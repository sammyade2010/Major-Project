from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Appliances(models.Model):
    description = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    prices = models.IntegerField(default=0)

    def __str__(self):
        return self.description

