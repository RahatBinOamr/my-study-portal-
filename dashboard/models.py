from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Notes(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=250)
  description =  RichTextField()


  def __str__(self) :
    return self.title
  class Meta:
    verbose_name = ("Notes")
    verbose_name_plural = ("Notes")
    
class HomeWork(models.Model):
  user= models.ForeignKey(User, on_delete=models.CASCADE)
  title= models.CharField(max_length=250)
  subject = models.CharField(max_length=250)
  description =  models.TextField()
  due = models.DateTimeField()
  is_finished = models.BooleanField(default=False)


class Todo(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=250)
    is_finished = models.BooleanField(default=False)




