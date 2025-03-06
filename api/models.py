from django.db import models

class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    job_role = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    date = models.DateField()
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_role}"

# Create your models here.
