from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

from CoinControllapp.forms import LoginForm, UserRegistrationForm
# Create your views here.




def home(request):
    return render(request, 'home.html')

#LOGIN FUNCIONALIDAD
def user_login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],
                                password= cd['password']
                                )# si no existe sera = none
            if user is not None:
                if user.is_active:  #asegurarse de que este activo para poder acceder a el
                    login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse('El usuario no esta activo')
                
            else: 
                return HttpResponse('La informacion no es correcta')
    else:
        form =LoginForm()
        return render(request,'login.html', {'form': form})





def register(request):
    error = ''  
    if request.method== 'POST':
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            try:
                new_user = user_form.save(commit=False) # de momento sera falso para que securicemos la contraseña
                new_user.set_password(
                user_form.cleaned_data['password']
                )# set_password encripta  la contraseña que se le pasa desde cleaned data => que recoge ya los datos validados 
                print(user_form.cleaned_data['password'],user_form.cleaned_data['password2'] )
                new_user.save()
                login(request,new_user)
                return redirect('home')
            except IntegrityError:
                error ='An exception occurred'
                print(error)
                return render(request, 'register.html',{'user_form':user_form,'error': error})
        else:
            #me devuelve los errores del metodo ya creado en forms.py
            error = user_form.errors.as_data()
            
            return render(request, 'register.html',{'user_form':user_form,'error': error})
        
    else: 
        
        user_form= UserRegistrationForm()
        return render(request, 'register.html',{'user_form':user_form,'error': error})
    
    
    
    
    
    
    
    
    
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        #INSTANCIA DEL FORM
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #autentificacion de usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                # Redirigir a la página de inicio
                return redirect('home')
            else:
                # Mostrar un mensaje de error si las credenciales son incorrectas
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request,'home.html')

