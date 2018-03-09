from django.conf.urls import url

from . import views
app_name='grade'
urlpatterns = [

	url(r'^create/grade/', views.grade_Create.as_view(), name='grade-create'),
	url(r'^(?P<last_name>[\w-]+)/$', views.ProfileDetailView.as_view(), name='detail'),

]