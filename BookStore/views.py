from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Add_Book_Cartoon,Add_Book_CHILDREN,Add_Book_FICTION,Add_Book_HISTORY
from django.urls import reverse
import datetime
#import Lib login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages
#Create your views here.
from .forms import Book_Form,Book_Form1,Book_Form2,Book_Form3

def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {"today" : today})

def Book_Page_cartoon(request):
    allItems = Add_Book_Cartoon.objects.all
    return render(request, 'Book_Page_cartoon.html',{'all' : allItems})

def Book_Page_cheilden(request):
    allItems = Add_Book_CHILDREN.objects.all
    return render(request, 'Book_Page_cheilden.html',{'all' : allItems})

def Book_Page_Fiction(request):
    allItems = Add_Book_FICTION.objects.all
    return render(request, 'Book_Page_Fiction.html',{'all' : allItems})

def Book_Page_history(request):
    allItems = Add_Book_HISTORY.objects.all
    return render(request, 'Book_Page_history.html',{'all' : allItems})

def Book_Page(request):
    return render(request, 'Book_Page.html')

def Service(request):
    return render(request, 'Service.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:        
        form = AuthenticationForm()
    return render(request,'login.html',{
        'form' : form,
    })
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def user_login(request):
    allItems = Add_Book_HISTORY.objects.all
    return render(request, 'userlogin.html')

def admin_login(request):
    return render(request, 'adminlogin.html')

def add_New_Book(request):
    form = Book_Form()

    if request.method == 'POST':
        form = Book_Form(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            messages.success(request,'Save success')
            return HttpResponseRedirect(reverse('Book_Page',kwargs={}))
        messages.error(request,'Save Failed')
    return render(request, 'add_NewBook.html', { 
        'form':form,
    })

def add_New_Book2(request):
    form = Book_Form1()

    if request.method == 'POST':
        form = Book_Form1(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            messages.success(request,'Save success')
            return HttpResponseRedirect(reverse('Book_Page',kwargs={}))
        messages.error(request,'Save Failed')
    return render(request, 'add_NewBook1.html', { 
        'form':form,
    })

def add_New_Book3(request):
    form = Book_Form2()

    if request.method == 'POST':
        form = Book_Form2(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            messages.success(request,'Save success')
            return HttpResponseRedirect(reverse('Book_Page',kwargs={}))
        messages.error(request,'Save Failed')
    return render(request, 'add_NewBook2.html', { 
        'form':form,
    })

def add_New_Book4(request):
    form = Book_Form3()

    if request.method == 'POST':
        form = Book_Form3(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            messages.success(request,'Save success')
            return HttpResponseRedirect(reverse('Book_Page',kwargs={}))
        messages.error(request,'Save Failed')
    return render(request, 'add_NewBook3.html', { 
        'form':form,
    })

