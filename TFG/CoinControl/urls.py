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
    path('mis_gastos/flitro_rango',views_gastos.filtrar_mis_gastos_rango_fecha, name='filtrar_mis_gastos_rango_fecha'),
    path('mis_gastos/flitro_mes',views_gastos.filtrar_mis_gastos_mes, name='filtrar_mis_gastos_mes'),
    path('mis_gastos/flitro_año',views_gastos.filtrar_mis_gastos_año, name='filtrar_mis_gastos_año'),
  #  path('mis_ingresos/',views.misingresos_view, name='mis_ingresos'),
    
    
]
