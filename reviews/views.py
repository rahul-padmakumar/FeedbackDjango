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
