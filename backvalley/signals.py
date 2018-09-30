import logging
logger = logging.getLogger(__name__)

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Startup
from .utils import get_lat_lon

@receiver(pre_save, sender=Startup, dispatch_uid='update_startup_location')
def update_location(sender, instance, **kwargs):
    lat, lon = 0.0, 0.0
    
    if (instance.address):
        lat, lon = get_lat_lon(instance.address)

    instance.lat = lat
    instance.lon = lon