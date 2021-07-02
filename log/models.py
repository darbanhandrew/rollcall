from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(blank=True, null=True)
    card_id = models.CharField(max_length=100)
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE)


class TimeTable(models.Model):
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recorded_at = models.DateTimeField(blank=True, null=True)
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE)
