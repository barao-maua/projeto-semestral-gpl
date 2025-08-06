"""
URL configuration for hotelTransilvania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls.conf import include
from app import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('suite-luxo/', app_views.suite_luxo, name='suite_luxo'),
    path('accomodations/', app_views.accomodations, name='accomodations'),
    path('reserva/', app_views.criar_reserva, name='reserva'),
    path('cadastro/', app_views.cadastrar_usuario, name='cadastro'),
    path('login/', app_views.login_usuario, name='login'),
    path('logout/', app_views.logout_usuario, name='logout'),
    path('avaliar/', app_views.criar_avaliacao, name='criar_avaliacao'),
    path('reservas/', app_views.minhas_reservas, name='minhas_reservas'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




