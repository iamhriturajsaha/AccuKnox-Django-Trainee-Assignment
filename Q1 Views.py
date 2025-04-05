from django.http import HttpResponse
from .models import Book
import logging

logger = logging.getLogger(__name__)

def create_book(request):
    logger.warning("Before save")
    Book.objects.create(title="Synchronous Signal Test")
    logger.warning("After save")
    return HttpResponse("Book created")

