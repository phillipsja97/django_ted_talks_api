from django.db import models

# Create your models here.

class Talks(models.Model):
  talk_id = models.AutoField(primary_key=True)
  talk_title = models.CharField(max_length=1500)
  talk_author = models.CharField(max_length=500)
  talk_href = models.CharField(max_length=1000)
  talk_image = models.CharField(max_length=500)