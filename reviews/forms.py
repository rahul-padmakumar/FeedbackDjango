from django import forms
from .models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = '__all__'
        labels = {
            'name': 'Your name',
            'rating': 'Your rating',
            'review': 'Your feedback'
        }
        error_messages = {
            'name': {
                'required': 'Please provide your name'
            },
            'rating':{
                'max_value': 'Rating max of 5 is supported'
            }
        }