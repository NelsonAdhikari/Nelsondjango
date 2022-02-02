from django.db import models

# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=200,)
     post_date = models.DateField(auto_now=True)
     def __str__ (self):
         return self.title


class Posts(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    img = models.ImageField(upload_to='Nelsondjango/')
    post_date=models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)