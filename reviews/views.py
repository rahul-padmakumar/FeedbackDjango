from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib import sessions
from django.urls import reverse

# Create your views here.

class ReviewView(CreateView):
    model = ReviewModel
    template_name="reviews/review.html"
    success_url="/success"
    form_class=ReviewForm
        

class SuccessView(TemplateView):
    template_name = "reviews/success.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you'
        return context
    
class AllReview(ListView):
    template_name = "reviews/all_reviews.html"
    model = ReviewModel
    context_object_name = "reviews"
    
class DetailReview(DetailView):
    template_name = "reviews/review_detail.html"
    model = ReviewModel
    context_object_name = "review"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.get_object()
        print(loaded_review.id)
        request = self.request
        fav_id = request.session['fav_review']
        print(fav_id)
        context["is_fav"] = fav_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, req):
        id = req.POST['review_id']
        print(id)
        req.session['fav_review'] = id
        return HttpResponseRedirect(reverse('review_detail', args=[id]))
        