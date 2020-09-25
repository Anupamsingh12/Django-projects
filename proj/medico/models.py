from django.db import models

class doctors(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='user_img')