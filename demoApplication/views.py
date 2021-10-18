from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render


# serializers
from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
# Token authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

"""
class Another(View):
    # books = Book.objects.filter(is_published=True)
    # books = Book.objects.filter(id=2)
    books = Book.objects.all()
    output = ''
    for book in books:
        output += f"We have '{book.title}' book with ID: '{book.id}', in database<br>"

    def get(self, request):
        return HttpResponse(self.output)
"""


def first(request):
    return HttpResponse('First message from views')


def show_template(request):
    books = Book.objects.all()
    return render(request, 'first_template.html', {'books': books})


# serializers
# Create a builtin views
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)  # Is a tupple need a coma
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
