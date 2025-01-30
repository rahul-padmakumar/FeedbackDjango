from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("success", views.SuccessView.as_view())
]
