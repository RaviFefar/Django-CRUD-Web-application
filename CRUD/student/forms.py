from django import forms
from student.models import Stud

class StudForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    email= forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email','help_text':'A valid email address'}))
    number= forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control','min':'0','placeholder':'Enter Number'}))

    checkbox = [('cricket','Cricket'),('barchhi_fek','Barchhi Fek'),('volleyball','Volleyball'),('basket_ball','Basket Ball')]

    hobbies = forms.MultipleChoiceField(required=False,widget= forms.CheckboxSelectMultiple, choices=checkbox)
    radiobutton = [('male','Male'),('female','Female')]
    gender = forms.ChoiceField(widget= forms.RadioSelect, choices=radiobutton)
    selectoption = [('bba','BBA'),('bca','BCA'),('bcom','BCOM'),('b.ed','B.ed')]
    education = forms.ChoiceField(widget= forms.Select(attrs={ "class":"form-control input_felid"}),choices=selectoption)
    image = forms.FileField(required=False,widget= forms.FileInput(attrs={ 'class':'form-control'}))
    age = forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control','min':'0','max':'100','placeholder':'Enter Age'}))

    class Meta:
        model = Stud
        fields = '__all__'
