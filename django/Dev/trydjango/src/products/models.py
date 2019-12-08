from django.db import models

#create your models here
class products():
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default="This is cool!")


