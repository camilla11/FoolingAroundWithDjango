from django.conf.urls import url

from . import views

# These urls get loaded my the urls.py in mysite - seperate and clean - cool
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<trackingtopic_id>[0-9]+)', views.results),
    url('addtrackingfields', views.addtrackingfields),
]