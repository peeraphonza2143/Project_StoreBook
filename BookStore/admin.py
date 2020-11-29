from django.contrib import admin

# Register your models here.
from .models  import  Add_Book_Cartoon,Add_Book_CHILDREN,Add_Book_FICTION,Add_Book_HISTORY


class BookAdmin(admin.ModelAdmin):
    list_display = ['NameBook', 'description', 'show_image']
    fieldsets = (
        (None, {'fields': ['NameBook', 'description', 'image']}
        ),     
    )

admin.site.register(Add_Book_Cartoon, BookAdmin)
admin.site.register(Add_Book_CHILDREN, BookAdmin)
admin.site.register(Add_Book_FICTION, BookAdmin)
admin.site.register(Add_Book_HISTORY, BookAdmin)