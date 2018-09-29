import logging
logger = logging.getLogger(__name__)

from .models import Startup

def update_location(sender, instance, **kwargs):
    logger.debug('Request finished!')
