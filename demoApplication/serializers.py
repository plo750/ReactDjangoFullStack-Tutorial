from rest_framework import serializers
from .models import Book, BookNumber, Character, Author


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        # We will create the serializers
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # We will create the serializers
        fields = ['id', 'name', 'surname']


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        # We will create the serializers
        fields = ['id', 'isbn_10', 'isbn_13']


class BookSerializer(serializers.ModelSerializer):
    # Allow to see the all object of BookNumber
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        # We will create the serializers
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number', 'characters', 'authors']


class BookMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # We will create the serializers
        fields = ['id', 'title']
