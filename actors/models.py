from django.db import models


NATIONALITIES= (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),



)
class Actor(models.Model):
    name=models.CharField(max_length=200)
    birthdate=models.DateField(null=True, blank=True)
    nationality=models.CharField(max_length=100,null=True,blank=True, choices= NATIONALITIES)

    def __str__(self):
        return self.name