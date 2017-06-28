from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_choropleth/$', views.get_choropleth, name='choropleth')
]
