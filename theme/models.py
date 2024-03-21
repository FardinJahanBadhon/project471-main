from django.db import models

# Create your models here.
#class Theme(models.Model):
    #color = models.CharField(max_length=1000)
    #user = models.CharField(max_length=1000)

    #def __str__(self):
        #return self.user
    
#from django.db import models

class Theme(models.Model):
    color = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.color