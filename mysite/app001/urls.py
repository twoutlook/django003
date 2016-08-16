from django.conf.urls import url

from . import views

app_name = 'app001'
urlpatterns = [
    url(r'^$', views.item000, name='index'),
    url(r'^item001/', views.item001, name='item001'),
    url(r'^item002/', views.item002, name='item002'),
    url(r'^item003/', views.item003, name='item003'),
    url(r'^item004/', views.item004, name='item004'),
    #url(r'^materials/', include('materials.urls')),
  
]