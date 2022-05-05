
from django.contrib import admin
from django.urls import include, path
from todolist import views

urlpatterns = [
    path('', include('todolist.urls')),
    path('cookie/', views.token_security, name="cookie")
    
]
