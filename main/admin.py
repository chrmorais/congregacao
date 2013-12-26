# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Congregacao, Grupo, Publicador

class GrupoAdmin(ModelAdmin):
    pass
admin.site.register(Grupo, GrupoAdmin)

class PublicadorAdmin(ModelAdmin):
    pass
admin.site.register(Publicador, PublicadorAdmin)