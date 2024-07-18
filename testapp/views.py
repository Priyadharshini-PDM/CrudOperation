from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import company
from .forms import Employees_form

def employe_list(request):
    emp = company.objects.all()
   
    context={
        'emplo':emp,
    }
    #extra = {}
    #extra['title'] = 'Employee'
    #context["title"] = "Employee"
   
    return render(request, 'list.html', context)
    
def employe_edit(request,pk):
    emp=company.objects.get(id=pk)
    form=Employees_form(instance=emp)
    if request.method =='POST':
       form=Employees_form(request.POST, instance=emp)
       if form.is_valid():
           emp.save()
       return redirect('list')
    context={
        'form':form
    }
    
    return render(request, 'edit.html', context)

def employe_create(request):
    # emp=Employees.objects.all()
    form=Employees_form()
    if request.method =='POST':
        form=Employees_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={
       
        'form':form
    }
    return render(request, 'create.html', context)

def employe_delete(request,pk):
    emp=company.objects.get(id=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('list')
    context={
        'emp':emp,
    }
    return render(request, 'delete.html', context)


