from django.shortcuts import render ,redirect
from student.forms import StudForm
from student.models import Stud
from django.http import HttpResponse
from django.contrib import messages

def create_stud(request):
    form = StudForm()
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = StudForm(request.POST, request.FILES)
        # Validate the form

        if form.is_valid():
            try:
                form.save()
                # After the operation was successful
                messages.success(request, "Created successful!")
                # redirect to some other page
                return redirect('/show_stud')
            except:
                message = "Something we are wrong!"
                form = StudForm()
            return render(request, 'create.html',{'message':message,'form':form})
    else:
        # Create an empty form instance
        form = StudForm()
    return render(request, 'create.html',{'form':form})

def show_stud(request):
    stud = Stud.objects.order_by('-id');
    return render(request, 'index.html', {'stud':stud})

def edit_stud(requst, id):
    stud = Stud.objects.get(id=id)
    return render(requst, 'edit.html',{'stud':stud})

def update_stud(request, id):
     stud = Stud.objects.get(id=id)
     if request.method == "POST" :
        form = StudForm(request.POST, request.FILES, instance = stud)
        if form.is_valid():
            form.save()
            # After the operation was Update
            messages.success(request, 'Update successful!')
            # redirect to some other page
            return redirect("/show_stud")
        # After the operation was fail
        message = 'Something we are wrong!'
        return render(request, 'edit.html',{'message':message,'stud':form})
     else:
         form = Stud.objects.get(id=id)
         stud = StudForm(instance = form)
         content = {'stud':stud,'id':id}
         return render(request, 'edit.html',content)

def delete_stud(request, id):
     stud = Stud.objects.get(id=id)
     stud.delete()
     # After the operation was Deleted
     messages.success(request, 'Deleted successful!')
     return redirect("/show_stud")
# Create your views here.
