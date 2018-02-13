from django.conf.urls import url

from . import views
app_name='myuser'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<last_name>[\w-]+)/$', views.GradeDetail.as_view(), name='grade'),

]