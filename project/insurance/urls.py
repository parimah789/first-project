from django.conf.urls import url
from .views import client_create, landing_page

urlpatterns = [
    url(r'^$', landing_page, name='home'),
]