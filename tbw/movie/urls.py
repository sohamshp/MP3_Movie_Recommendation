from django.conf.urls import url
from . import views

app_name="movie"

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^searchres/', views.searchres, name="searchres")
]