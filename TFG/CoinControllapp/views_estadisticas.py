import pandas as pd
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Gasto
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from datetime import datetime
from django.http import HttpResponse
from .models import Gasto
from itertools import cycle
import matplotlib
matplotlib.use('Agg')
# sin esto me da warnings y se cae
from django.utils.translation import gettext as _

from django.db.models import Q



from django.urls import reverse




def mis_estadisticas(request):
    fecha_actual = timezone.now()
    mes = _(fecha_actual.strftime("%B")) #traducir el mes
    return render(request,'mis_estadisticas.html',{'mes': mes})
def gastoInicio(request ,mes ):
    año =request.GET.get('año')
    if año is None or año== '':
      año= None
   
    return render(request,'gastos_inicio_estadisticas.html', {'mes': mes, 'año': año})

def filtrar_gasto(request):
    filtro_mes = request.GET.get('filtro_mes')
    filtro_año = request.GET.get('filtro_año')
    if filtro_año is None:
      filtro_año= ' '
    return render(request,'gastos_estadisticas_filtrado.html', {'filtro_mes': filtro_mes, 'filtro_año': filtro_año}) 
def obtener_gastos_mes(request,mes):  
    
    año = request.GET.get('año')

    if mes:
        meses_espanol_a_numero = {
            'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
            'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12,
        }
        mes_actual = meses_espanol_a_numero.get(mes.lower(), None)
    else:
        mes_actual = datetime.now().month  # Mes actual si no se proporciona

    # Convertir el año a número si se proporciona
    if año:
        try:
            año_actual = int(año)
        except ValueError:
            año_actual = datetime.now().year  # Año actual si la conversión falla
    else:
        año_actual = datetime.now().year  # Año actual si no se proporciona

        
    # Obtén los gastos del mes actual
    # Obtener todos los gastos para el mes actual
    gastos_mes_actual = Gasto.objects.filter(
        (Q(fecha__month=mes_actual, fecha__year=año_actual) & Q(pagoUnico=False)) |  # Gastos no recurrentes del mes actual
        (Q(fecha__month__lte=mes_actual, fechaFin__month__gte=mes_actual) |(Q(fecha__year=año_actual, fecha__month=mes_actual)) ) # Gastos recurrentes que se superponen con el mes actual
    )

    # Crea un DataFrame de Pandas con los datos de los gastos
    data = {
        'Categoria': [g.categoria for g in gastos_mes_actual],
        'Cantidad': [g.cantidad for g in gastos_mes_actual],
        'Dia': [g.fecha.day for g in gastos_mes_actual]
    }
    df = pd.DataFrame(data)

    # Agrupa los gastos por categoría y calcula la suma de las cantidades
    df_agrupado = df.groupby('Categoria')['Cantidad'].sum().reset_index()
    
    # Definir una lista de colores y un ciclo de colores
    colors = ['skyblue', 'lightgreen', 'coral', 'lightpink', 'lightyellow', 'lightgray', 'lightblue', 'violet']
    color_cycle = cycle(colors)

    # Asignar colores de manera cíclica a cada barra
    bar_colors = [next(color_cycle) for _ in range(len(df_agrupado))]
    # Crea la gráfica de barras
    plt.figure(figsize=(8, 4))
    plt.bar(df_agrupado['Categoria'], df_agrupado['Cantidad'], color=bar_colors,width=0.4)
    plt.xlabel('')
    plt.ylabel('')
   # plt.title('Gastos del mes actual por categoría')
    plt.xticks()
    plt.tight_layout()

    # Guardar la imagen en un objeto BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Devolver la imagen como respuesta HTTP
    return HttpResponse(buf, content_type='image/png')