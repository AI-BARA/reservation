from django.db import models
from django.utils import timezone

class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    people = models.IntegerField(default=0)
    serial = models.IntegerField(default=0)
    solt_butter = models.IntegerField(default=0)
    curry = models.IntegerField(default=0)
    caramel = models.IntegerField(default=0)
    chocolate = models.IntegerField(default=0)
    enter = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.name[:10])
