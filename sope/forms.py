
from django import forms 
from .models import Employee
from datetime import date


EmpTitles = ["Manager","HR","Intern"]
Dep_Choice = []
for i in EmpTitles:
    Dep_Choice.append((i,i))
class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
    
   

    Name = forms.CharField(required = True,max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))

    DOB = forms.DateField(widget=forms.TextInput
                         (attrs={'class':'form-control','type': 'date','max':date.today()}))
    
    DOJ = forms.DateField(widget=forms.TextInput
                         (attrs={'class':'form-control','type': 'date','max':date.today()}))
                
    Department = forms.ChoiceField(choices=Dep_Choice,
                                  widget = forms.Select
                                  (attrs = {'class':'form-control'}))

    Post = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))

    Address = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    
    City = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    
    Country = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    
    Zipcode = forms.IntegerField( widget= forms.NumberInput
                                (attrs={'class':'form-control',"min":"100000","max":"999999"}))
                                
    
    State = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control'}))

    Active = forms.BooleanField(required = False,widget= forms.CheckboxInput
                                    (attrs={'class': 'required checkbox form-control'})) 
   

    Leave_count = forms.IntegerField(widget= forms.NumberInput
                           (attrs={'class':'form-control','value' : 0,'readonly': True}))     

    On_leave = forms.BooleanField(required = False,widget= forms.CheckboxInput
                                (attrs = {'class':'form-control'}))                                  


    