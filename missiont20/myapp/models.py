from django.db import models

# Create your models here.

class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
class Doctorinfo(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_image=models.ImageField(upload_to='doctor/')
    doctor_specialization=models.CharField(max_length=100)
    def __str__(self):
        return self.doctor_name