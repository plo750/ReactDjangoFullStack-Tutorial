from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.
class Another(View):

    # books = Book.objects.filter(is_published=True)
    # books = Book.objects.filter(id=2)
    books = Book.objects.all()
    output = ''
    for book in books:
        output += f"We have '{book.title}' book with ID: '{book.id}', in database<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
