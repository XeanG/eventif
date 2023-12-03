from django.apps import AppConfig

class ContatoConfig(AppConfig):
    name = 'contact'
    verbose_name = 'Gerenciamento de Contatos'

    def ready(self):
       import contact.signals