from django.db import models


# Create your models here.
class Blanks(models.Model):
    email = models.EmailField(max_length=40, null=True)
    password = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=40)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.surname}'

    def get_absolute_url(self):
        return f'{self.pk}'

