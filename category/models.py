from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)


class Post(models.Model):
    post = models.CharField(max_length=50)
