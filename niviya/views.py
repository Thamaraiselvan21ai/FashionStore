from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
class log:
    def __init__(self):
        self.nu = 0
obj = log()

def indexhtml(request):
    if obj.nu == 1:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
    elif obj.nu == 2:
        template = loader.get_template('products.html')
        return HttpResponse(template.render())
    elif obj.nu == 3:
        template = loader.get_template('categories.html')
        return HttpResponse(template.render())           
    elif obj.nu == 4:
        template = loader.get_template('contact.html')
        return HttpResponse(template.render())        
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
def returnhome(request,nu):
    obj.nu = nu
    return redirect(indexhtml)
def returnproducts(request,nu):
    obj.nu = nu
    return redirect(indexhtml)
def returncategori(request,nu):
    obj.nu = nu
    return redirect(indexhtml)
def returncontact(request,nu):
    obj.nu = nu
    return redirect(indexhtml)


    

def loginhtml(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# def indexhtml(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

# def indexhtml1(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

# def categorieshtml(request):
#     template = loader.get_template('categories.html')
#     return HttpResponse(template.render())

# def contacthtml(request):
#     template = loader.get_template('contact.html')
#     return HttpResponse(template.render())

# def Niviyahtml(request):
#     template = loader.get_template('Niviya.html')
#     return HttpResponse(template.render())

def signhtml(request):
    template = loader.get_template('sign.html')
    return HttpResponse(template.render())

# def productshtml(request):
#     template = loader.get_template('products.html')
#     return HttpResponse(template.render())

def back(request):
    return redirect('loginhtml')
    
def createuser(request):
    users = request.POST['username']
    password1 = request.POST['password1']
    password2= request.POST['password2']

    if password1 == password2:
        load = signup(username = users,password = password1)
        load.save()
        return redirect('loginhtml')
    else:
        return HttpResponse("password are not match")
def signin(request):
    email = request.POST['emailid']
    password = request.POST['pass']
    data = signup.objects.filter(username=email)
    if data:
        data = signup.objects.get(username=email)
        if data.password == password:
            return redirect('indexhtml')
        else:
            return HttpResponse("Wrong password")
#     else:
#         return HttpResponse("Incorect password")
    
# def home(request):
#     return redirect('indexhtml')
# def products(request):
#     return redirect('productshtml')

