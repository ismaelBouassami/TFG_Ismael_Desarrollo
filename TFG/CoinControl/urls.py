"""
URL configuration for CoinControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CoinControllapp import views
from CoinControllapp import views_gastos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('mis_gastos/',views_gastos.misgastos_view, name='mis_gastos'),
    path('mis_gastos/unicos',views_gastos.gastosUnicos_view,name='gastos_unico'),
    path('mis_gastos/recurrente',views_gastos.gastosRecurrente_view,name='gastos_recurrente'),
    
    
    
    
    
    
    
    path('mis_gastos/recurrentes/flitro_rango',views_gastos.filtrar_mis_gastos_rango_fecha_Recurrente, name='filtrar_mis_gastos_rango_fecha_Recurrente'),
    path('mis_gastos/recurrentes/flitro_mes',views_gastos.filtrar_mis_gastos_mes_Recurrente, name='filtrar_mis_gastos_mes_Recurrente'),
    path('mis_gastos/recurrentes/flitro_año',views_gastos.filtrar_mis_gastos_año_Recurrente, name='filtrar_mis_gastos_año_Recurrente'),
 
    path('mis_gastos/unicos/flitro_rango',views_gastos.filtrar_mis_gastos_rango_fecha_Unico, name='filtrar_mis_gastos_rango_fecha_Unico'),
    path('mis_gastos/unicos/flitro_mes',views_gastos.filtrar_mis_gastos_mes_Unico, name='filtrar_mis_gastos_mes_Unico'),
    path('mis_gastos/unicos/flitro_año',views_gastos.filtrar_mis_gastos_año_Unico, name='filtrar_mis_gastos_año_Unico'),
    
    
    path('mis_gastos/unicos/new',views_gastos.new_gasto_unico, name='new_gasto_unico'),
    path('mis_gastos/recurrentes/new',views_gastos.new_gasto_recurrente, name='new_gasto_recurrente'),
    
  #  path('mis_ingresos/',views.misingresos_view, name='mis_ingresos'),
    
    
]
