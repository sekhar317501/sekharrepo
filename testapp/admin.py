from django.contrib import admin
from testapp.models import Book

class BookAdmin(admin.ModelAdmin):
    list_diplay=['title','author','pages','price']
admin.site.register(Book,BookAdmin)
