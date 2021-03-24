from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Mark
import mysql.connector
from django.contrib import messages
from .forms import registerform,markform
# Create your views here.
def home(request):
    return render(request,'login/adminHome.html')

def register(req):
    form=registerform()
    if req.method=='POST':
        form=registerform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(req,'login/staffReg.html',context)
def info(req,pk_test):
    user=User.objects.get(id=pk_test)
    mark=user.mark_set.all()
    context={'user':user,'mark':mark}
    return render(req,'login/view.html',context)

def update(req,pk_test):
    user = User.objects.get(id=pk_test)
    form = registerform(instance=user)
    if req.method=='POST':
        form=registerform(req.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(req, 'login/update.html', context)

def updatemark(req,pk_test):
    mark = Mark.objects.get(mid=pk_test)
    form = markform(instance=mark)
    context = {'form': form}
    return render(req, 'login/updatemark.html',context)

def delete(req,pk):
    user = User.objects.get(id=pk)
    if req.method=="POST":
        user.delete()
        return redirect('/')
    context={'item':user}
    return render(req,'login/delete.html',context)

def markupdate(req):
    form=markform()
    if req.method=='POST':
        form=markform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(req,'login/markupdate.html',context)
