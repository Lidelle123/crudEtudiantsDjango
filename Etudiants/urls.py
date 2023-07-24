from django.contrib import admin
from django.urls import path
from Etudiants.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app, name='app'),
    path('students/', index, name='index'),
    #path('create/', create, name='create'),
    path('create/',studentCreate , name='create'),
    path('students/delete/<int:student_id>/',studentDelete , name='delete'),
    path('students/update/<int:student_id>/',studentUpdate , name='update'),
    path('register/', register, name='register'),
    path('accounts/login/', login, name='login'),
    path('logout/', deconnexion, name='logout'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
