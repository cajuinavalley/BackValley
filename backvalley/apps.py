from django.apps import AppConfig

# from django.db.models.signals import post_save
# from .models import Startup
# from .signals import update_location

# import logging
# logger = logging.getLogger(__name__)

class BackvalleyConfig(AppConfig):
    name = 'backvalley'

    # def ready(self):
    #     post_save.connect(update_location, sender=Startup)