from django.apps import AppConfig


class BackvalleyConfig(AppConfig):
    name = 'backvalley'

    def ready(self):
        import backvalley.signals