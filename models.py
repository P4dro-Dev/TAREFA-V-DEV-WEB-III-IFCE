from django.db import models

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail', blank=True, null=True)
    mini_curriculo = models.TextField('Mini currículo', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome
