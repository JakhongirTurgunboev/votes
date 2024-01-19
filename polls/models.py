from django.db import models

# Create your models here.
from users.models import MyUser


class Vote(models.Model):
    VOTE_CHOICES = (
        ('d', 'democrats'),
        ('r', 'republicans'),
    )
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    vote_to = models.CharField(max_length=1, choices=VOTE_CHOICES)


