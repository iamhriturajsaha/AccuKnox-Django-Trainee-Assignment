from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

class Book(models.Model):
    title = models.CharField(max_length=100)

class LogEntry(models.Model):
    message = models.CharField(max_length=255)

@receiver(post_save, sender=Book)
def book_saved_handler(sender, instance, created, **kwargs):
    LogEntry.objects.create(message=f"Book created: {instance.title}")
    logger.warning("LogEntry created inside signal.")



