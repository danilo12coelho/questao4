from django.contrib import admin

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Coleçao'
admin.site.site_title = 'Emprestimo de Revistinhas'

from core.models import Colecao, Caixa
from core.models import Amigo, Emprestimo
from core.models import Revista

class ColecaoInline(admin.TabularInline):
    model = Colecao
    max_num = 1


class CaixaInline(admin.TabularInline):
    model = Caixa
    max_num = 1


class RevistaAdmin(admin.ModelAdmin):
    list_display = ('numero_edicao', 'ano',)
    inlines = [
        ColecaoInline, CaixaInline
    ]


class AmigoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_mae', 'telefone', 'grupo_amigo')


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('data_emprestimo', 'data_devolucao', 'amigo')


admin.site.register(Revista, RevistaAdmin)
admin.site.register(Colecao)
admin.site.register(Caixa)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
