# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from stone.app.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from stone.app.models import Pessoa, Projeto, Version, Feature




# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()

    #chama func que gera projetos
    projetos = get_projetos()
    
    form_class = ContactForm
    return render(request, 'index.html',{'STATIC_URL': settings.STATIC_URL,'MEDIA_URL':settings.MEDIA_URL ,'form': form_class,'pessoas': pessoas,"projetos": projetos})


def mensagem_enviada(request):
    #url mostra mensagem de enviado com sucesso
    pessoas = Pessoa.objects.all()

    #chama func que gera projetos
    projetos = get_projetos()
    
    form_class = ContactForm
    return render(request, 'index.html',{'STATIC_URL': settings.STATIC_URL,'MEDIA_URL':settings.MEDIA_URL ,'form': form_class,'pessoas': pessoas,"projetos": projetos})

def send_email(request):
    subject = request.POST.get('contact_name')
    #gera a mensagem
    message = "Setor: " + request.POST.get('contact_setor') + "\n\n"
    message += "Qual o impacto da demanda?\n" + request.POST.get('contact_impacto') + "\n\n"
    message += "Qual o resultado esperado?\n" + request.POST.get('contact_resultado') + "\n\n"
    message += "Como você pretende medir o sucesso deste novo produto ou feature?\n" + request.POST.get('contact_sucesso') + "\n"

    from_email = request.POST.get('contact_email')
    message = message + "\n from: "+ str(from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['uxteamstone@gmail.com'])
            return HttpResponseRedirect('/mensagem_enviada/#contact')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Mensagem enviada com sucesso')

    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def get_projetos():
    #retorna projetos
    projetos = Projeto.objects.all()
    #adiciona no objeto projetos as versões e features
    for projeto in projetos:
        versoes = Version.objects.filter(projeto=projeto)
        for v in versoes:
            v.features = Feature.objects.filter(versao=v) 
        projeto.versoes = versoes
    
    return projetos