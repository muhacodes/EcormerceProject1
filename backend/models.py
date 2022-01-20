from django.db import models
from account.models import User

# Create your models here.

class Testimonials(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username            = models.CharField(max_length=50, null=True)
    message             = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username