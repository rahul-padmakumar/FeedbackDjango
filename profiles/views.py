from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
class ProfileView(View):
    def get(self, req):
        return render(req, "profiles/profile.html")
    def post(self, req):
        print(req.FILES['image'])
        return HttpResponseRedirect("/profiles")