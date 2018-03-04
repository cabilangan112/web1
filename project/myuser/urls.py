from django.conf.urls import url
from . import views
app_name='myuser'
urlpatterns = [
#	url(r'^$', views.index, name='index'),
	url(r'^bscsfirst/$', views.bscsfirst.as_view(), name='firstyear'),
	url(r'^bscssecond/$', views.bscssecond.as_view(), name='secondyear'),
	url(r'^bscsthird/$', views.bscsthird.as_view(), name='thirdyear'),
	url(r'^bscsfourth/$', views.bscsfourth.as_view(), name='fourthyear'),

	url(r'^signup/', views.SignUpView.as_view(), name='signup'),
	url(r'^signup/student/', views.RegisterView.as_view(), name='student'),
	url(r'^signup/faculty/', views.FacultyRegisterView.as_view(), name='faculty'),


	url(r'^(?P<slug>[\w-]+)/$', views.StudentUpdateView.as_view(), name='edit'),
]