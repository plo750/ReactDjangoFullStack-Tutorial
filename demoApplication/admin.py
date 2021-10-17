from django.contrib import admin

# Register your models here.
from demoApplication.models import Book


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'is_published', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']  # Where to search
