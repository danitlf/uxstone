# coding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):

    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome *', 'id':'name', 'data-validation-required-message':'Escreva um nome.'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail *', 'id':'email', 'data-validation-required-message':'Digite um e-mail.'}))
    contact_setor = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Setor *', 'id':'setor', 'data-validation-required-message':'Escreva seu setor.'}))
    contact_impacto = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Qual o impacto da demanda? *', 'id':'impacto', 'data-validation-required-message':'Escreva o impacto.'})
    )
    contact_resultado = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Qual o resultado esperado? *', 'id':'resultado', 'data-validation-required-message':'Escreva o resultado esperado.'})
    )
    contact_sucesso = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Como você pretende medir o sucesso deste novo produto ou feature? *', 'id':'sucesso', 'data-validation-required-message':'Escreva como pretende medir o sucesso.'})
    )