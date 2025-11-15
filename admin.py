from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')
