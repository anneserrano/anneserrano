from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^accueil/$', views.home),
]


'''from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^accueil$', views.home),  # Accueil du menu
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]'''

