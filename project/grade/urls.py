from django.conf.urls import url

from . import views
app_name='grade'
urlpatterns = [

#template View
	url(r'^Year/$', views.Year.as_view(), name='Year'),


#Create View
	url(r'^create/grade/', views.grade_Create.as_view(), name='grade-create'),

	url(r'^print/', views.GeneratePdf.as_view(), name='print'),
#Detail View
	url(r'^1st/(?P<last_name>[\w-]+)/$', views.ProfileDetailView1.as_view(), name='detail1'),
	url(r'^2nd/(?P<last_name>[\w-]+)/$', views.ProfileDetailView2.as_view(), name='detail2'),
	url(r'^3rd/(?P<last_name>[\w-]+)/$', views.ProfileDetailView3.as_view(), name='detail3'),
	url(r'^4rt/(?P<last_name>[\w-]+)/$', views.ProfileDetailView4.as_view(), name='detail4'),

]