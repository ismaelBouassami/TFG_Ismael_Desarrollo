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


@login_required
def misgastos_view(request):
    # Gastos del usuario
    gastos = Gasto.objects.filter(usuario=request.user)
    
    return render(request, 'mis_gastos.html', {'gastos': gastos})
    
    
    
@login_required
def filtrar_mis_gastos_rango_fecha(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__range=[fecha_inicio, fecha_fin])
    print(gastos)
    return render(request, 'mis_gastos.html', {'gastos': gastos})


@login_required
def filtrar_mis_gastos_año(request):
    año = request.GET.get('filtro_año')
    añoNum = int(año)
    errorfiltrarAño='Todo correcto'
    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user,  fecha__year=añoNum)
    if not gastos.exists():
      errorfiltrarAño='No se encotraron resultados del año '+ año
    print(gastos)
    return render(request, 'mis_gastos.html', {'gastos': gastos, 'errorfiltrarAño':errorfiltrarAño})



@login_required
def filtrar_mis_gastos_mes(request):
  
    # Mapear el nombre del mes al número de mes
    mes_numero = request.GET.get('filtro_mes')
    print('Numero del mes '+ str(mes_numero))
    # Filtrar los gastos por fecha
    gastos = Gasto.objects.filter(usuario=request.user, fecha__month=mes_numero)
    print(gastos)
    return render(request, 'mis_gastos.html', {'gastos': gastos})