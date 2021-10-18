from django.contrib import admin

# Register your models here.
from demoApplication.models import Book, BookNumber, Character, Author


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description'] # Otherwise we not see the OneToOneField
    list_display = ['title', 'is_published', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']  # Where to search


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)