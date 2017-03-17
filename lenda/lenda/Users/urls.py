from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.items_Listing, name = 'home'),
    url(r'^new/$', views.items_New, name='new'),
    url(r'^(?P<id>\d+)/$', views.items_Detail, name= 'detail')
]