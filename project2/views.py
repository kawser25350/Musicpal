from django.shortcuts import render
from album.models import Album
from musician.models import Musician 


def home(request):
    a=Album.objects.all()
    m=Musician.objects.all()
    return render(request,'pages/home.html',{'adata':a,'mdata':m})