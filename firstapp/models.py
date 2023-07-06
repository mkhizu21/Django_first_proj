from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName=models.CharField(max_length=122)
    LastName=models.CharField(max_length=122)
    Username=models.CharField(max_length=122)
    Email=models.CharField(max_length=122)
    reason=models.TextField()

    def __str__(self):
        return self.FirstName