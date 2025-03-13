from django.db import models

# Model for Theme
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='media/themes/')
    caption = models.TextField()