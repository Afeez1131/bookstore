import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('book_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    book = models.ForeignKey(
        Book,                related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review
