from django.urls import path
from .views import ContactFormView, ContactListContacts, DeleteContact
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('write/', ContactFormView.as_view(), name='contact'),
    path('list/', login_required(ContactListContacts.as_view(),login_url='/user/login/'), name='contact_list'),
    path('delete/<int:pk>/', login_required(DeleteContact.as_view(),login_url='/user/login/'), name='contact_delete'),
]