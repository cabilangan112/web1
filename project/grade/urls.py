from django.conf.urls import url

from . import views
app_name='grade'
urlpatterns = [
	url(r'^bscsfirst/$', views.bscsfirst.as_view(), name='firstyear'),
	url(r'^bscssecond/$', views.bscssecond.as_view(), name='secondyear'),
	url(r'^bscsthird/$', views.bscsthird.as_view(), name='thirdyear'),
	url(r'^bscsfourth/$', views.bscsfourth.as_view(), name='fourthyear'),
	
	url(r'^(?P<last_name>[\w-]+)/$', views.ProfileDetailView.as_view(), name='detail'),
]