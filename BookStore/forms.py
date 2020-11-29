from django import forms
from .models import Add_Book_Cartoon,Add_Book_CHILDREN,Add_Book_FICTION,Add_Book_HISTORY

class Book_Form(forms.ModelForm):
    class Meta:
        model = Add_Book_Cartoon
        exclude = ['NAMEBOOk']

class Book_Form1(forms.ModelForm):
    class Meta:
        model = Add_Book_CHILDREN
        exclude = ['NAMEBOOk']

class Book_Form2(forms.ModelForm):
    class Meta:
        model = Add_Book_FICTION
        exclude = ['NAMEBOOk']

class Book_Form3(forms.ModelForm):
    class Meta:
        model = Add_Book_HISTORY
        exclude = ['NAMEBOOk']


    