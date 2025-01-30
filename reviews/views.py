from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.http import HttpResponseRedirect
from django.views import View

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
        

class SuccessView(View):
    def get(self, req):
        return render(req, "reviews/success.html")
