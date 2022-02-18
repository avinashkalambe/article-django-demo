from django.urls import path
from .views import home, about, details, add, update, delete


urlpatterns = [
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('details/<int:pk>/', details, name= 'details'),  #127.0.0.1:8000/details/1
    path('add/', add, name= 'add'),
    path('update/<int:pk>/', update, name= 'update'),
    path('delete/<int:pk>/',delete, name='delete')
]