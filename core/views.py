from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import FBForm

# Create your views here.
from .models import Feedback

#function first parameter is request(convention, but any thing can be used)
def home(request):
    #return HttpResponse("Hello World")

    x = Feedback.objects.all()
    context = {
        'data':x
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Feedback.objects.create(
            title = title,
            description = description
        )
        return redirect('homepage')
    return render(request,'create.html', {})

def update(request, user_id):
    print(user_id)
    feedback_obj = get_object_or_404(Feedback, id=user_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        #Feedback.objects.filter(id=user_id).update(title)

        feedback_obj.title = title
        feedback_obj.description = description
        feedback_obj.save()

        return redirect('homepage')
    return render(request,'create.html', {})

def delete(request, user_id):
    obj = get_object_or_404(Feedback, id=user_id)
    obj.delete()
    return redirect('homepage')

def feedback_create(request):
    if request.method == "GET":
        c = {'form': FBForm()}
        return render(request,"create.html",c)
    else:
        form = FBForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            return redirect('home')
        else:            
            return render(request,"create.html",c)