from django.shortcuts import render,HttpResponseRedirect,get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
#from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def register(request):
    form= userForm()
    if request.method == "POST":
        form= userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "votre compte a ete bien creer")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    context={
        'form':form
    }
            
    return render(request,'register.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request)
            messages.success(request, "Bienvenue")
            return redirect('')
        else:
            messages.error(request, "erreur d'authentification")
    return render(request,'login.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')

def app(request):
    return render(request, 'app.html')

#@login_required
def index(request):
    students= Student.objects.all()
    
    page=request.GET.get('page',1)
    paginate= Paginator(students, 5)
    try:
       students=paginate.page(page)
    except PageNotAnInteger:
        students=paginate.page(1)
    except EmptyPage:
       students=paginate.page(Paginator.num_pages)
        
    
    context={
        'students':students
    }
    
    return render(request, 'student/index.html', context)

def create(request):
    filieres=Filiere.objects.all()
    context={
        'filieres':filieres
    }
    return render(request, 'student/create.html',context)

def studentCreate(request):
    message=" "
    form = studentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=studentForm()
        message="Ajout reussi"
        context = {
        'form':form,
        'message':message
        }
    else:
        message="L'etudiant n'a pas ete ajoute"
        form=studentForm()
        context = {
        'form':form,
        'message':message
        }
        return render(request, 'student/create.html', context)
      
    
      
    return render(request, 'student/create.html', context)


# Fonction de modification d'étudiant
def studentUpdate(request, student_id):
    # Récupérer l'étudiant à modifier
    student = get_object_or_404(Student, pk=student_id)
    
    # Vérifier la méthode de requête HTTP
    if request.method == 'POST':
        # Si la méthode est POST, récupérer les données du formulaire
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        # Si la méthode est GET, pré-remplir le formulaire avec les données de l'étudiant à modifier
        form = studentForm(instance=student)
    
    # Afficher le formulaire de modification
    context = {'form': form}
    return render(request, 'student/update.html', context)
  
        
    
def studentDelete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('index'))
    context = {'student': student}
    return render(request, 'student/delete.html', context)
    

    
        
        
        
        
    
        
    
