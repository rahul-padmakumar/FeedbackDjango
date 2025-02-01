from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm

def save_file(file):
    print(file.name)
    with open(f"temp/{file.name}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# Create your views here.
class ProfileView(View):
    def get(self, req):
        form = ProfileForm()
        return render(
            req,
            "profiles/profile.html",
            {'form': form}
        )
    def post(self, req):
        form = ProfileForm(req.POST, req.FILES)
        if form.is_valid():
            file = req.FILES['user_image']
            print(f"File uploaded is: {file}")
            save_file(file)
            return HttpResponseRedirect("/profiles")
        else: 
            print(f"FORM NOT{form.errors}")
            return render(
                req,
                "profiles/profile.html",
                {'form': form}
            )