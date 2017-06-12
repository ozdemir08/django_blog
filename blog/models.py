from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('pub_date')
    author = models.CharField(max_length=30)
    preview = models.CharField(max_length=300)
    content = models.CharField(max_length=10000)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title