from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def home(request):
    return render(request,'base.html')
def rec(request):
    form= models.StudentReg.objects.all()
    return render(request,'records.html',{'data':form})
def reg(request):
    if request.method == 'POST':
        form = forms.StudentRegForms(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            mm = forms.StudentRegForms(auto_id=1,label_suffix='') 
            message = "Data add Sucessfully"
            return render(request,'registration.html',{'form': mm,'mes':message})                    
        else:
            form = forms.StudentRegForms(auto_id=1,label_suffix='') 
            message = "Data not add Sucessfully Formate not acceptable"
            return render(request,'registration.html',{'form': form,'mes':message})                    
            
    form = forms.StudentRegForms(auto_id=1,label_suffix='')
    return render(request,'registration.html',{'form': form})

def updateview(request,pk):
    form = models.StudentReg.objects.get(id=pk)
    return render(request,'update.html',{'data':form ,'id':pk})
    
def update(request,pk):
    data = models.StudentReg.objects.get(id=pk)
    if request.method =="POST":
        if data.name :
            data.name = request.POST['name']
            print(data.name)
        if data.email :
            data.email = request.POST['email']
            print(data.email)
        if data.mobile :
            data.mobile = request.POST['mobile']
        if data.gender :
            data.gender = request.POST['gender'] 
        if data.dob :
            data.dob = request.POST['date']  
        data.save()
        message= 'data id submitted'
        return redirect('/rec/')

def deletefun(request,pk):
    data = models.StudentReg.objects.get(id=pk)
    data.delete()
    return redirect('/rec/')
               
    
    
    
    
    
    
    
    
    
    

    
    

    