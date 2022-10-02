from django.db import models

# Create your models here.
class GeneratedVoice(models.Model):
    image=models.ImageField(blank=True,upload_to="images")
    voice=models.FileField(blank=True,upload_to="voices")
