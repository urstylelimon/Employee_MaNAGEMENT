from django.shortcuts import render
from.models import Employee, Role, Depertment

def index(request):
    return render(request,'index.html')

def show(request):
    emp = Employee.objects.all()
    content = {'emp':emp}
    return render(request,'show.html',content)

def add(request):
    return render(request,'add.html')

def delete(request):
    return render(request,'delete.html')

def update(request):
    return render(request,'update.html')