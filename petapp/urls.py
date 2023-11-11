from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('howitworks',views.howitworks,name='howitworks'),
    path('contact',views.contact,name='contact'),
    path('findmypet',views.findmypet,name='findmypet'),
    
    

]