from django.db import models

# Create your models here.

#Student form imported to contact page
#models.py->views.py->contact method
class Student(models.Model):
    image=models.ImageField(upload_to='student_images/', blank=True)
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    admission_number = models.CharField(max_length=50, default="2345")
    gender = models.CharField(max_length=10, choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
        ]
    )
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name
