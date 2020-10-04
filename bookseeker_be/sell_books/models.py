from django.db import models

class booksell_model(models.Model):
    name=models.CharField(max_length=50)
    bookpicture=models.ImageField()
    age = models.IntegerField(blank=True)
    description=models.CharField(max_length=500)
    status=models.DateField(blank=True)


    def __str__(self):
        return self.name