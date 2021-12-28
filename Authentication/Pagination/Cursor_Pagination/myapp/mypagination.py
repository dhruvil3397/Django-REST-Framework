from django.core.paginator import Page
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'