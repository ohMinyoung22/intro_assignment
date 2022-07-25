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
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),
    path('edit_comment/<int:id>', edit_comment, name="edit_comment"),
    path('update_comment/<int:id>', update_comment, name="update_comment"),
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('my_like/<int:user_id>', my_like, name='my_like'),
    path('dislike_toggle/<int:post_id>/', dislike_toggle, name="dislike_toggle"),
    path('my_dislike/<int:user_id>', my_dislike, name='my_dislike'),
]