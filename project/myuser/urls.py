from django.conf.urls import url

from . import views
app_name='myuser'
urlpatterns = [
#	url(r'^$', views.index, name='index'),
	#BSCS LIST
	url(r'^bscsfirst/$', views.bscsfirst.as_view(), name='firstyear'),
	url(r'^bscssecond/$', views.bscssecond.as_view(), name='secondyear'),
	url(r'^bscsthird/$', views.bscsthird.as_view(), name='thirdyear'),
	url(r'^bscsfourth/$', views.bscsfourth.as_view(), name='fourthyear'),
	




	#DEtail
	url(r'^(?P<last_name>[\w-]+)/$', views.GradeDetail.as_view(), name='grade'),

]