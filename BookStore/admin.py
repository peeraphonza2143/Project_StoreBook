from django.contrib import admin

# Register your models here.
from .models  import  Add_Book_Cartoon


class BookAdmin(admin.ModelAdmin):
    list_display = ['NameBook', 'description', 'show_image']
    fieldsets = (
        (None, {'fields': ['NameBook', 'description', 'image']}
        ),     
    )

admin.site.register(Add_Book_Cartoon, BookAdmin)