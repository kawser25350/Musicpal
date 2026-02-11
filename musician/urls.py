from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.musician_home,name='musician_home'),
    path('add_musician',views.add_musician,name='add_musician'),
    path('edit_musician/<int:id>',views.edit_musician,name='edit_musician'),
    path('delete_musician/<int:id>',views.delete_musician,name='delete_musician')
]
