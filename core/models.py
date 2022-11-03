from django.db import models
from django.utils.timezone import get_current_timezone

# Create your models here.
class NotificationHistory(models.Model):
    fcm_token = models.TextField()
    title = models.CharField(max_length=150)
    body = models.TextField()
    icon = models.ImageField(upload_to='', null=True, blank=True)
    image = models.ImageField(upload_to='', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.datetime.astimezone(get_current_timezone()).strftime(f'%d-%B-%Y %I:%M:%S')