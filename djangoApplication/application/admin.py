from django.contrib import admin
from application.models import Student

# Register your models here.
#connecting the student form to the database
admin.site.register(Student)
