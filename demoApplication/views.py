from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# serializers
from rest_framework import viewsets
from .serializers import BookSerializer
# Token authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



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


def showTemplate(request):
    books = Book.objects.all()
    return render(request, 'first_template.html', {'books': books})


# serializers
# Create a builtin views
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,) # Is a tupple need a coma
    permission_classes = (IsAuthenticated,)