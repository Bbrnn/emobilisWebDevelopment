from django import forms

from application.models import Student

class StudentForm(forms.ModelForm):
    class Meta:

        model = Student
        fields = '__all__'

        #styling the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Age'}),
            'admission_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Admission Number'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Gender'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Course'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'title': 'Upload Image',})

        }


