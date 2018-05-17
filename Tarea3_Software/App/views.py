

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import Seguridad
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.
seguridad = Seguridad()

def home(request):
        template = loader.get_template('App/choices.html')
        return HttpResponse(template.render(None,request))


def index(request):

    validacion=[1,1,""]
    text = ''
    context = {
        'validacion': validacion,
        'text': text,
    }

    if request.method =='POST':
        user =request.POST.get('Email')
        clave1 =request.POST.get('password')
        clave2 =request.POST.get('confirm_password')
        validacion = seguridad.registrarUsuario(user,clave1,clave2)
        text = validacion[2]
        context = {
        'validacion': validacion,
        'text': text,
        }

        if validacion[0] == 1 and validacion[1]== 1:
            #template = loader.get_template('correo/index.html')
            #return HttpResponseRedirect('correo')
            return HttpResponseRedirect('http://127.0.0.1:8000/login/')
        else:
            template = loader.get_template('App/index.html')
            return HttpResponse(template.render(context,request))
            #return HttpResponseRedirect('http://127.0.0.1:8000/correo/')
    else:
            template = loader.get_template('App/index.html')
            return HttpResponse(template.render(context,request))
        


def login(request):
    validacion=[1,""]
    text = ''
    context = {
        'validacion': validacion,
        'text': text,
    }

    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('Email')
        passwd = request.POST.get('password')
        validacion = seguridad.IngresarUsuario(user, passwd)
        text = validacion[1]
        context = {
        'validacion': validacion,
        'text': text,
        }

        if validacion[0] == 1:
            #messages.success(request, validarRegistro[1])
            return HttpResponseRedirect('http://127.0.0.1:8000/user/')
        else:
            template = loader.get_template('App/login.html')
            return HttpResponse(template.render(context,request))
    else:
        template = loader.get_template('App/login.html')
        return HttpResponse(template.render(context,request))


def user(request):
        template = loader.get_template('App/logout.html')
        return HttpResponse(template.render(None,request))

def vacio(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/home/')
