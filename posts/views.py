from django.shortcuts import render, redirect
from .models import Category
from django.contrib import messages
# Create your views here.

def category(request):
    if request.method=='GET':
        cat = Category.objects.all()#select *
        context ={
             'categories':cat,
         }
        return render(request,'category.html')
    else:
        t= request.POST['categorytitle']
        try:
            cat = Category(title=t)
            cat.save()
            messages.add_message(request,messages.SUCCESS,"saved")
        except Exception as e:
            messages.add_message(request,messages.ERROR,e)
        return redirect('category')
