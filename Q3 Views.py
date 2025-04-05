from django.http import HttpResponse
from django.db import transaction
from .models import Book
import logging

logger = logging.getLogger(__name__)

def create_book_view(request):
    try:
        with transaction.atomic():
            Book.objects.create(title="Transactional Signal Test")
            raise Exception("Simulated exception to trigger rollback")
    except Exception as e:
        logger.warning(f"Exception occurred: {e}")
    return HttpResponse("Done")
