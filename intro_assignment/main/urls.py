from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name= 'showmain'),
    path('mainpage/', showpage, name= 'showpage'),
    path('<int:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name='create_comment'),
]