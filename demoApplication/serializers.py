from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # We will create the serializers
        fields = ['title', 'is_published', 'description', 'price']
