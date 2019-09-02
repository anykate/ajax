from django.urls import path
from . import views


app_name = 'anapp'

urlpatterns = [
    path('', views.index, name='index'),
    # path('ajax/', views.contactPage, name='contact_get'),
    path('ajax/contact/', views.contact, name='contact'),
]
