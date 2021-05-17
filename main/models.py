from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200, null=False)
    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    flyer = models.ImageField(default='default.png', blank=False)
    registration = models.TextField()



    def __str__(self):
        return self.name