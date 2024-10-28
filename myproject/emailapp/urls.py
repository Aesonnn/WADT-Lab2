# emailapp/urls.py

from django.urls import path
from .views import send_email, person_list, add_person, delete_person

urlpatterns = [
    path('', send_email, name='send_email'),
    path('add_person/', add_person, name='add_person'),
    path('people/', person_list, name='person_list'),
    path('delete_person/<int:person_id>/', delete_person, name='delete_person'),
]