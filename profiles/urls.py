from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('list', views.ProfileListView.as_view())
]
