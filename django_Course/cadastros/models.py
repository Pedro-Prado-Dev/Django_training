from django.db import models

# Create your models here.
class Cidade(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class Estado(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     def __str__(self):
#         return self.name