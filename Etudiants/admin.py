from django.contrib import admin
from .models import *

   # def __str__(self):
       # pass

   # class Meta:
        #db_table = ''
       ##verbose_name_plural = 'ModelNames'

# Register your models here.
class AdminFiliere(admin.ModelAdmin):
    list_display =('name','description')
    
class AdminStudent(admin.ModelAdmin):
    list_display =('name','email','phone','birthdate','filiere_id')
    
class AdminCour(admin.ModelAdmin):
    list_display =('name','description','filiere_id')
    
class AdminNote(admin.ModelAdmin):
    list_display =('student_id','cour_id','value')
    
    
admin.site.register(Filiere, AdminFiliere)
admin.site.register(Student, AdminStudent)
admin.site.register(Cour, AdminCour)
admin.site.register(Note, AdminNote)