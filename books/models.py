from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)            
    author = models.CharField(max_length=100)           
    published_date = models.DateField()                 
    pages = models.PositiveIntegerField()               
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank=True) 
    category = models.CharField(max_length=255, null=True, blank=True) 



    def __str__(self):
        return self.title
