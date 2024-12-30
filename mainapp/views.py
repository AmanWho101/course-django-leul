from django.shortcuts import render, redirect
from .models import *
# Create your views here.
# index => home
def index(request):
    all_data = Student.objects.all()
    context={'all_data':all_data}
    return render(request, "crud/index.html",context)
# edit page
def edit(request,id):
    edit = Student.objects.get(id=id)
    context={'data':edit}
    return render(request, "crud/edit.html",context)
# delete
def delete(request,id):
    delete_data = Student.objects.get(id=id)
    delete_data.delete()
    return redirect('/firstcrud')
# create page
def create(request):
    return render(request, "crud/create.html")
# create page data=>store db
def store(request):
    if request.POST:
        store_data = Student(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            age=request.POST.get('age'),
            address=request.POST.get('address'),
        )
        store_data.save()
    return redirect('/firstcrud')
# edit page data=>store db
def update(request,id):
    update_data = Student.objects.get(id=id)
    update_data.fname = request.POST.get('fname')
    update_data.lname = request.POST.get('lname')
    update_data.age = request.POST.get('age')
    update_data.address = request.POST.get('address')
    update_data.save()
    return redirect('/firstcrud')