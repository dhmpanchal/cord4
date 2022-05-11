from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add_todo', add_todo, name='add_todo'),
    path('edit_todo/<int:id>', edit_todo, name='edit_todo'),
    path('delete_todo/<int:id>', delete_todo, name='delete_todo'),
]