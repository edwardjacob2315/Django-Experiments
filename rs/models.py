from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=150)
    age=models.IntegerField(default=20)
    experience=models.IntegerField(default=1)
    specialist=models.CharField(max_length=100,default='pilot name')
    def __str__(self):
        return self.name

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.CharField(max_length=150)
    age=models.IntegerField(default=20)
    job=models.CharField(max_length=100)
    domisili=models.CharField(max_length=100)

    def __str__(self):
        return self.name    

# class Appointment(models.Model):
#     doctors=models.ForeignKey(Doctor,on_delete=models.CASCADE)
#     patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date_app = models.DateField()
#     bill = models.IntegerField(blank=True, null=True)