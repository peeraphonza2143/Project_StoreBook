from django import forms
from .models import Add_Book_Cartoon

class Book_Form(forms.ModelForm):
    class Meta:
        model = Add_Book_Cartoon
        exclude = ['NAMEBOOk']
    