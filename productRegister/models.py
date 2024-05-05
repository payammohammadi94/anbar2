from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from jalali_date import datetime2jalali

class productRegistrationModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    first_last_name = models.CharField(max_length=200)
    
    prudoct_name = models.CharField(max_length=200)
    prudoct_code = models.CharField(max_length=200,blank=True,null=True)
    
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    
    
    
    #برای اینکه تحویل داده یا نه
    status = models.BooleanField(default=False)
    
    def get_jalali_date_create(self):
        return datetime2jalali(self.create)
    
    def get_jalali_date_update(self):
        return datetime2jalali(self.update)
    
    
    def __str__(self):
        return "{}-{}".format(self.first_last_name,self.prudoct_name)
    

