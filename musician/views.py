from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def musician_home(request):
    m=models.Musician.objects.all()
    return render(request,'pages/musician_home.html',{'data':m})

def add_musician(request):
    if request.method == 'POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_home')
    form=forms.MusicianForm
    return render(request,'pages/musician_add_musician.html',{'form':form})

def edit_musician(request,id):
    m=models.Musician.objects.get(pk=id)
    form=forms.MusicianForm(instance=m) 

    if request.method == 'POST':
        form=forms.MusicianForm(request.POST,instance=m) 
        if form.is_valid():
            form.save()
            return redirect('musician_home')
    return render(request,'pages/musician_add_musician.html',{'form':form})

def delete_musician(request,id):
    m=models.Musician.objects.get(pk=id)
    m.delete();
    return redirect('musician_home')