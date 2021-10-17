from rest_framework import serializers
from .models import Book, BookNumber


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        # We will create the serializers
        fields = ['id', 'isbn_10', 'isbn_13']


class BookSerializer(serializers.ModelSerializer):
    # Allow to see the all object of BookNumber
    number = BookNumberSerializer(many=False)

    class Meta:
        model = Book
        # We will create the serializers
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number']
