from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
    path('user_login', login_required(views.user_login,login_url='/login'), name='user_login'),
     path('admin_login', login_required(views.admin_login,login_url='/login'), name='admin_login'),
    path('admin_login/addnewbook', login_required(views.add_New_Book,login_url='/login'), name='add_New_Book'),
    path('admin_login/addnewbook1', login_required(views.add_New_Book2,login_url='/login'), name='add_New_Book2'),
    path('admin_login/addnewbook2', login_required(views.add_New_Book3,login_url='/login'), name='add_New_Book3'),
    path('admin_login/addnewbook3', login_required(views.add_New_Book4,login_url='/login'), name='add_New_Book4'),
    path('service', views.Service, name='Service'),
    path('contact', views.contact, name='contact'),
    path('service/book', views.Book_Page, name='Book_Page'),
    path('service/book/cartoon', views.Book_Page_cartoon, name='Book_Page_cartoon'),
       path('service/book/cheilden', views.Book_Page_cheilden, name='Book_Page_cheilden'),
          path('service/book/Fiction', views.Book_Page_Fiction, name='Book_Page_Fiction'),
             path('service/book/history', views.Book_Page_history, name='Book_Page_history'),
    
]