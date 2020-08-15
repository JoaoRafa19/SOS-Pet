from django.contrib import admin
from .models import Pet
# Register your models here.


'''
# admin.site.register(Pet)
só registra a classe no admin

'''

'''
Registra a classe no admin com o decorator @admin.register(Classe)
e  o list_display seleciona os campos que vai mostrar no administrador
'''

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome','cidade']