from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("success", views.SuccessView.as_view()),
    path("reviews", views.AllReview.as_view()),
    path("review/<int:pk>", views.DetailReview.as_view(), name="review_detail")
]
