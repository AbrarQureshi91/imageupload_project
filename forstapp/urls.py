from django.urls import path
from forstapp import views
urlpatterns = [
     path('', views.home , name='home'),
     path('mail/', views.send_mail , name= 'send_mail' )
]
