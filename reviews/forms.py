from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Name", 
        max_length=10,
        error_messages={
            'required': 'Your name must not be empty',
            'max_length': 'Max length should be 10'
        }
    )
    #review = forms.CharField(label="Your Review")
    #rating = forms.IntegerField(min_value=1, max_value=5, label="Rating")