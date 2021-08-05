from django.contrib.auth import get_user_model
from django.db import models

CATEGORY_CHOICES = [
    ('P', 'Pets'),
    ('D', 'Dance'),
    ('F', 'Fun'),
]


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stories'
    )
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=200, choices = CATEGORY_CHOICES, default='F')
    content = models.TextField()
    image = models.URLField()
    