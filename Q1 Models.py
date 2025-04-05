from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import logging

logger = logging.getLogger(__name__)

class Book(models.Model):
    title = models.CharField(max_length=100)

@receiver(post_save, sender=Book)
def book_saved_handler(sender, instance, created, **kwargs):
    logger.warning("🔁 Signal started")
    time.sleep(5)  # Simulate a slow signal
    logger.warning("✅ Signal completed")
