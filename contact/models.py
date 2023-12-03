from django.db import models

class Contact_model(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Mensagem')
    response = models.TextField(verbose_name='Resposta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return self.name

