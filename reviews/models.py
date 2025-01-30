from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class ReviewModel(models.Model):
    name = models.CharField(max_length=10)
    review = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
