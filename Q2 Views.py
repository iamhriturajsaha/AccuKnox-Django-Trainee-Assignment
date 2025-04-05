from django.http import HttpResponse
from .models import Book
import threading
import logging

logger = logging.getLogger(__name__)

def create_book(request):
    logger.warning(f"🧵 Caller thread ID: {threading.get_ident()}")
    Book.objects.create(title="Same Thread Test")
    return HttpResponse("Book created")


