from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user_id = models.IntegerField(max_length= 20, null= True)
    post = models.CharField(max_length= 200, null= True)
    def __str__(self):
        return self.post