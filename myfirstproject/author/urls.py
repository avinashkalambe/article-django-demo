from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView


urlpatterns = [
    path('', AuthorListView.as_view(), name='list_authors'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='detail_author'),
    path('create/', AuthorCreateView.as_view(), name='create_author'),
    path('update/<int:pk>/', AuthorUpdateView.as_view(), name='update_author'),
    path('delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete_author'),
]