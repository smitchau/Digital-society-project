from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True , max_length = 30)
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20)    #chairmen / society member
    isActive = models.BooleanField(default = False)
    Created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email + " | " + self.role   

class Chairmen(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 11)
    blockno = models.CharField(max_length = 3)
    houseno = models.CharField(max_length = 4)
    pic = models.FileField(upload_to="media/uplode",default="default.png")
    

    def __str__(self):
        return self.firstname + " | "+self.blockno
    
class Member(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 11)
    blockno = models.CharField(max_length = 3)
    houseno = models.CharField(max_length = 4)
    occupation = models.CharField(max_length = 20)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length = 3)
    vehicle_detail = models.CharField(max_length = 20)
    pic = models.FileField(upload_to="media/uplode",default="default.png")
    def __str__(self):
        return self.firstname + " | "+self.lastname