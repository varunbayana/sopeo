from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForms

# Create your views here.

def home(request):
    emplist = Employee.objects.all()
    Active_count = 0
    for emp in emplist:
        if emp.Active == True:
            Active_count+= 1
    context = {'Active_count': Active_count,'emplist': emplist}
    return render(request, 'home.html',context)

def createEmployee(request):
    
    if request.method == "POST":
        
        # emp = Employee.objects.create(Name = request.POST.get('Name'),Post = request.POST.get('Post'),Address = request.POST.get('Address'),City = request.POST.get('City'),Country = request.POST.get('Country'),Zipcode = request.POST.get('Zipcode'),State = request.POST.get('State'),Active = request.POST.get('Active'),Leave_count = request.POST.get('Leave_count') )
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()

    form = EmployeeForms()
    context = {'form': form }

    return render(request, 'createEmployee.html',context)

def EditEmployee(request,pk):
    emp = Employee.objects.get(pk = pk)
    form = EmployeeForms(instance = emp)
    if request.method == "POST":

        form = EmployeeForms(request.POST,instance = emp)
        if form.is_valid():
            if(form.On_leave):
                form.Leave_count +=1
            elif form.On_leave == False:
                 form.Leave_count = form.Leave_count

            form.save()
            return redirect('list')
        
    context = {'form':form}
    return render(request, 'EditEmployee.html',context)

def EmployeeList(request):
    emplist = Employee.objects.all()
    emplist = emplist.values()
    context = { 'emplist': emplist }
    return render(request, 'employeeList.html', context = context)
