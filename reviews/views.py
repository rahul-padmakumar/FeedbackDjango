from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

# Create your views here.

class ReviewView(FormView):
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/success"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        

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