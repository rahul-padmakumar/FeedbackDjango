from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class ReviewView(View):
    def get(self, req):
        form = ReviewForm()
        return render(req, "reviews/review.html", {"form":form})
    
    def post(self, req):
        form = ReviewForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
        else:
            return render(req, "reviews/review.html", {"form":form})
        

class SuccessView(TemplateView):
    template_name = "reviews/success.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you'
        return context
    
class AllReview(TemplateView):
    template_name = "reviews/all_reviews.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['reviews'] = ReviewModel.objects.all()
        return context
    
class DetailReview(TemplateView):
    template_name = "reviews/review_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs["id"]
        context['review'] = ReviewModel.objects.get(id = id)
        return context