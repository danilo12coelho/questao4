from django.db import models

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"


class Revista(models.Model):
    numero_edicao = models.IntegerField('Numero da Edição')
    ano = models.IntegerField('Ano')

    def __str__(self):
        return "Revista Numero {}".format(self.numero_edicao)

    class Meta:
        verbose_name_plural = 'Revistas'
        verbose_name = 'Revista'


class Colecao(models.Model):
    nome = models.CharField('Nome', max_length=50)
    tipo_edicao = models.ForeignKey('Revista', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Coleções'
        verbose_name = 'Coleção'


class Caixa(models.Model):
    numero = models.IntegerField('Numero')
    etiqueta = models.CharField('Etiqueta', max_length=50)
    cor = models.CharField('Cor', max_length=15)
    caixa = models.ForeignKey('Revista', on_delete=models.CASCADE)

    def __str__(self):
        return "Caixa Numero: {}".format(self.numero)

    class Meta:
        verbose_name_plural = 'Caixas'
        verbose_name = 'Caixa'


class Amigo(models.Model):
    GrupoAmigo_choices = {
        ('', (
            ('PRÉDIO', 'Prédio'),
            ('ESCOLA', 'Escola'),
        ),
         )
    }

    nome = models.CharField('Nome', max_length=50)
    nome_mae = models.CharField('Nome da Mae', max_length=50)
    telefone = models.CharField('Telefone', max_length=20)
    grupo_amigo = models.CharField('Grupo de Amigo', max_length=10, choices=GrupoAmigo_choices, default='')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Amigos'
        verbose_name = 'Amigo'


class Emprestimo(models.Model):
    data_emprestimo = models.DateField('Data de Emprestimo')
    data_devolucao = models.DateField('Data de Devolução')
    amigo = models.ForeignKey('Amigo', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = 'Emprestimos'
        verbose_name = 'Emprestimo'
