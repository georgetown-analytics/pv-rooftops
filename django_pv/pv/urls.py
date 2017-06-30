from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_choropleth/$', views.get_choropleth, name='choropleth'),
	url(r'^get_visualizations/$', views.get_visualizations, name='visualizations'),
	url(r'^get_heatmap/$', views.get_heatmap, name='heatmap')
]
