from django.shortcuts import render
from .forms import ReviewForm
from .models import ReviewModel
from django.http import HttpResponseRedirect

# Create your views here.
def review(req):
    if req.method == "POST":
        form = ReviewForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
        else:
            print(form.errors)  
    else:    
        form = ReviewForm()
        print("I am here")
    return render(req, "reviews/review.html", {"form": form})

def success(req):
    return render(req, "reviews/success.html")
