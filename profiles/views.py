from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView

def save_file(file):
    print(file.name)
    with open(f"temp/{file.name}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# Create your views here.
class ProfileView(CreateView):
    template_name = "profiles/profile.html"
    model = ProfileModel
    fields = '__all__'
    success_url = "/profiles"

class ProfileListView(ListView):
    template_name="profiles/list_profile.html"
    model = ProfileModel
    context_object_name = "profiles"