# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from stone.app.models import Pessoa
from stone.app.models import Projeto
from stone.app.models import Version
from stone.app.models import Feature
from django.contrib import admin

# Register your models here.


class ProjetosAdmin(admin.ModelAdmin):

    
    list_display = ('nome','descricao',)
    list_editable = ()
    list_editable = ()
    search_fields = ('nome',)
    fields = ()
    
    
    
admin.site.register(Projeto, ProjetosAdmin)

class VersoesAdmin(admin.ModelAdmin):
    
    list_display = ('versao','titulo','projeto','data',)
    list_editable = ()
    list_editable = ()
    search_fields = ('versao','titulo','projeto','data',)
    fields = ()
    
    
    
admin.site.register(Version, VersoesAdmin)

class FeatureAdmin(admin.ModelAdmin):

    
    list_display = ('feature','versao',)
    list_editable = ()
    list_editable = ()
    search_fields = ('feature','versao',)
    fields = ()
    
    
    
admin.site.register(Feature, FeatureAdmin)

class PessoaAdmin(admin.ModelAdmin):

    
    list_display = ('nome','cargo',)
    list_editable = ()
    list_editable = ()
    search_fields = ('nome','cargo',)
    fields = ()
    
    
    
admin.site.register(Pessoa, PessoaAdmin)