from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg/$', views.reg),
    url(r'^login/$', views.login),
    url(r'^allquotes/logout/$', views.logout),
    url(r'^allquotes/$', views.allquotes),
    url(r'^allquotes/addquote/(?P<id>\d+)$', views.addquote),
    url(r'^allquotes/myfav/(?P<id>\d+),(?P<q>\d+)$', views.myfav),
    url(r'^allquotes/myfavdelete/(?P<id>\d+)$', views.myfavdelete),
     url(r'^allquotes/postview/(?P<id>\d+)$', views.postview),

]
