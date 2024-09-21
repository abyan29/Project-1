from django.apps import AppConfig


class MyfirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myFirstapp'

    def ready(self):
        import myFirstapp.signals
