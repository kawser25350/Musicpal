from django.shortcuts import render,redirect
from .import forms
from .models import Album

# Create your views here.
def album_home(request):
    data=Album.objects.all()
    return render(request,'pages/album_home.html',{'data':data})

def add_album(request):
    if request.method == 'POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_home')
    form=forms.AlbumForm
    return render(request,'pages/album_add_album.html', {'form':form})

def edit_album(request,id):
    a=Album.objects.get(pk=id)
    form=forms.AlbumForm(instance=a)

    if request.method =='POST':
        form=forms.AlbumForm(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('album_home')
    return render(request,'pages/album_add_album.html', {'form':form})

def delete_album(request,id):
    a=Album.objects.get(pk=id)
    a.delete()
    return redirect('album_home')