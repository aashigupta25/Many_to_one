from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    blog_title = models.CharField(max_length = 100)
    blog_category = models.CharField(max_length = 100)
    blog_publish_date = models.DateField()
