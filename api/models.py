from django.db import models


class file(models.Model):
    file=models.FileField(upload_to='file')
    
    
class CSVData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.name