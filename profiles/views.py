from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

def save_file(file):
    print(file.name)
    with open(f"temp/{file.name}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# Create your views here.
class ProfileView(View):
    def get(self, req):
        return render(req, "profiles/profile.html")
    def post(self, req):
        save_file(req.FILES['image'])
        return HttpResponseRedirect("/profiles")