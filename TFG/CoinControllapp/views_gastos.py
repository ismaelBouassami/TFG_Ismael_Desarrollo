from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Gasto
from calendar import month_name
from datetime import datetime
from django.db.models import Q


@login_required
def misgastos_view(request):
    
    
    return render(request, 'mis_gastos.html')
    
    
    
@login_required
def filtrar_mis_gastos_rango_fecha_Unico(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__range=[fecha_inicio, fecha_fin],fechaFin__isnull= True)
    print(gastos)
    return render(request, 'mis_gastos_unicos.html', {'gastos': gastos})


@login_required
def filtrar_mis_gastos_año_Unico(request):
    año = request.GET.get('filtro_año')
    añoNum = int(año)
    errorfiltrarAño=''
    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__year=añoNum,fechaFin__isnull= True)
    if not gastos.exists():
      errorfiltrarAño='No se encotraron resultados del año '+ año
    print(gastos)
    return render(request, 'mis_gastos_unicos.html', {'gastos': gastos, 'errorfiltrarAño':errorfiltrarAño})



@login_required
def filtrar_mis_gastos_mes_Unico(request):
  
    # Mapear el nombre del mes al número de mes
    mes_numero = request.GET.get('filtro_mes')
    print('Numero del mes '+ str(mes_numero))
    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user, fecha__month=mes_numero,fechaFin__isnull= True)
    print(gastos)
    return render(request, 'mis_gastos_unicos.html', {'gastos': gastos})


    
@login_required
def filtrar_mis_gastos_rango_fecha_Recurrente(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__range=[fecha_inicio, fecha_fin],fechaFin__isnull= False)
    print(gastos)
    return render(request, 'mis_gastos_recurrentes.html', {'gastos': gastos})


@login_required
def filtrar_mis_gastos_año_Recurrente(request):
    año = request.GET.get('filtro_año')
    añoNum = int(año)
    print( añoNum)
    errorfiltrarAño=''
    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__year=añoNum,fechaFin__isnull= False)
    if not gastos.exists():
      errorfiltrarAño='No se encotraron resultados del año '+ año
    print(gastos)
    return render(request, 'mis_gastos_recurrentes.html', {'gastos': gastos, 'errorfiltrarAño':errorfiltrarAño})



@login_required
def filtrar_mis_gastos_mes_Recurrente(request):
    # Obtener el número del mes seleccionado en el filtro
    mes_numero = request.GET.get('filtro_mes')
    
    # Filtrar los gastos por fecha que caen dentro del mes seleccionado
    gastos = Gasto.objects.filter(
        (Q(fecha__month__lte=mes_numero) & Q(fechaFin__month__gte=mes_numero)), usuario=request.user
    )
    
    print(gastos)
    return render(request, 'mis_gastos_recurrentes.html', {'gastos': gastos})


@login_required
def gastosUnicos_view(request):
    # Gastos del usuario
    gastos = Gasto.objects.filter(usuario=request.user,fechaFin__isnull= True)
    
    return render(request, 'mis_gastos_unicos.html', {'gastos': gastos})


@login_required
def gastosRecurrente_view(request):
    # Gastos del usuario
    gastos = Gasto.objects.filter(usuario=request.user,fechaFin__isnull= False)
    print('Gastos view ')
    print(gastos)
    return render(request, 'mis_gastos_recurrentes.html', {'gastos': gastos})



def new_gasto_unico(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        categoria = request.POST['categoria']
        fecha = request.POST['fecha']
         
        gasto = Gasto(nombre=nombre, cantidad=cantidad, categoria=categoria, fecha=fecha, pagoUnico=True, usuario= request.user)
        gasto.save()
        return redirect('gastos_unico')  
    else:
        return render(request, 'new_gasto_unico.html') 
    
    
    
def new_gasto_recurrente (request):
    error = ''
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        categoria = request.POST['categoria']
        fecha = request.POST['fecha']
        fechaFin = request.POST['fechaFin']
        
        if fecha >= fechaFin:
            error ='La fecha inico no puede ser superior a la fecha fin'
            return render(request, 'new_gasto_recurrente.html',{ 'error': error }) 
        
        gasto = Gasto(nombre=nombre, cantidad=cantidad, categoria=categoria, fecha=fecha,fechaFin=fechaFin, pagoUnico=False, usuario= request.user)
        gasto.save()
        return redirect('gastos_recurrente')  
    else:
        return render(request, 'new_gasto_recurrente.html',{'error': error }) 