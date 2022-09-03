from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    cat_title = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title