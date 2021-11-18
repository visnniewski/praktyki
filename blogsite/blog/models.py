import datetime

from django.db import models
from django.utils import timezone

class Title(models.Model):
    title_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title_text

class Description(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=1200)

    def __str__(self):
        return self.description_text