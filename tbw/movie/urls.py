from django.conf.urls import url
from . import views

app_name="movie"

urlpatterns = [
    url(r'^$',views.index, name="index"),

    url(r'^searchres/$', views.searchres, name="searchres"),

    url(r'^mov/(?P<m_id>[0-9]+)/$', views.movieView, name="movieView"),

    url(r'^user/(?P<u_id>[0-9]+)/recommend/$', views.predict, name="recommend"),

    url(r'^signup/$', views.signUpView, name="signup"),

    url(r'user/$', views.userView, name="user"),

    url(r'category/$', views.catView, name="category"),


    url(r'^addrate/', views.addRatings),

    url(r'^user/(?P<u_id>[0-9]+)/$', views.predict, name="predict"),

    url(r'^unrate/$', views.makeUnrated, name="unrate"),

    url(r'^imdb/$', views.getImdb, name="imdb"),
]