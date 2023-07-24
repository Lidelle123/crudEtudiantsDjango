from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.s
class Filiere(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    
    class Meta:
        verbose_name =("Filiere")
        verbose_name_plural =("Filieres")

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    #phone = PhoneNumberField(unique=True, blank=True)
    birthdate = models.DateField()
    filiere_id = models.ForeignKey(Filiere, verbose_name=(""), on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None, null=True)
    
    class Meta:
        verbose_name =("Student")
        verbose_name_plural =("Students")

    def __str__(self):
        return self.name
    
class Cour(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    filiere_id = models.ForeignKey(Filiere, verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name =("Cour")
        verbose_name_plural =("Cours")

    def __str__(self):
        return self.name


class Note(models.Model):
    student_id = models.ForeignKey(Student, verbose_name=(""), on_delete=models.CASCADE)
    cour_id = models.ForeignKey(Cour, verbose_name=(""), on_delete=models.CASCADE)
    value = models.FloatField(max_length=2)
    
    class Meta:
        verbose_name =("Note")
        verbose_name_plural =("Notes")
    