# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Projeto(models.Model):

    imagem = models.ImageField(_('Imagem:'),null=True, blank=True, upload_to= 'uploads')
    nome = models.TextField(_('Nome'),max_length=100,blank=True)
    descricao = models.TextField(_('descrição'),max_length=100,blank=True)
    def __unicode__(self):
        return (self.nome)

class Version(models.Model):

    versao = models.CharField(_('Numero da Versão'),max_length=100,null=True, blank=True)
    titulo = models.CharField(_('titulo'),max_length=100,null=True, blank=True)
    projeto = models.ForeignKey('Projeto')
    data = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return (self.versao + " "+ self.projeto.nome)

class Feature(models.Model):

    feature = models.TextField(_('Mudança Feita'),max_length=1000,blank=True)
    versao = models.ForeignKey('Version')
    def __unicode__(self):
        return (self.feature)

class Pessoa(models.Model):

     foto = models.ImageField(_('Foto:'),null=True, blank=True, upload_to= 'uploads')
     nome = models.TextField(_('Nome'),max_length=100,blank=True)
     cargo = models.TextField(_('Cargo'),max_length=100,blank=True)
     def __unicode__(self):
        return (self.nome)