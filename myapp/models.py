from django.db import models

# Create your models here.

class Students(models.Model):
    Name = models.CharField(max_length=50)
    Img = models.ImageField(upload_to='media', blank=True)
    Enrollment_no = models.TextField(blank=True)
    Scholar_no = models.IntegerField(primary_key=True)
    Class = models.TextField()
    Section = models.TextField(blank=True)
    Dob = models.DateField(null=True)
    Year = models.IntegerField()
    Email = models.EmailField()
    Father_name = models.CharField(max_length=50, blank=True)
    Mother_name = models.CharField(max_length=50, blank=True)
    Mobile_no = models.TextField()
    Address = models.TextField()
    City = models.TextField()
    Sem1 = models.ImageField(upload_to='media', blank=True, default="Not Found")
    Sem2 = models.ImageField(upload_to='media', blank=True, default="Not Found")
    Sem3 = models.ImageField(upload_to='media', blank=True, default="Not Found")
    Sem4 = models.ImageField(upload_to='media', blank=True, default="Not Found")

    def __str__(self):
        return self.Name+" "+self.Enrollment_no+" "+self.Class