from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ERROR(models.Model):
    error_desc  = models.CharField(max_length=30)
    # error_image = models.ImageField()
    error_sol = models.CharField(max_length=50)
    error_ref = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.error_desc

class Comment(models.Model):
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    error = models.ForeignKey(ERROR, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment



