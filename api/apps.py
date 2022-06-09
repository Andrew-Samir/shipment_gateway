from django.apps import AppConfig
from django.conf import settings

class AutofoxConfig(AppConfig):
    name = 'api'
    def ready(self):
        pass
