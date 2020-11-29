from django.db import models
from django.utils.html import format_html

# Create your models here.
class Add_Book_Cartoon(models.Model):
    NameBook = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True

class Add_Book_FICTION(models.Model):
    NameBook = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True

class Add_Book_CHILDREN(models.Model):
    NameBook = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True

class Add_Book_HISTORY(models.Model):
    NameBook = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True