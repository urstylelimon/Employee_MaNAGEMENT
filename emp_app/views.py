from django.shortcuts import render
from.models import Employee, Role, Depertment
from datetime import datetime
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def show(request):
    emp = Employee.objects.all()
    content = {'emp':emp}
    return render(request,'show.html',content)

def add(request):
    if request.method == 'POST':
        fname = request.POST.get['fname']
        lname = request.POST.get['lname']
        department = int(request.POST.get['department'])
        salary = request.POST.get['salary']
        bonus = request.POST.get['bonus']
        role = int(request.POST.get['role'])
        Phone = request.POST.get['Phone']
        new_emp = Employee(first_name= fname, last_name=lname, salary=salary, bonus=bonus, phone=Phone, dept_id = department, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')


    
    return render(request,'add.html')

def delete(request):
    return render(request,'delete.html')

def update(request):
    return render(request,'update.html')