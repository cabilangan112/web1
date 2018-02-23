from django.conf.urls import url

from . import views
app_name='grade'
urlpatterns = [
	url(r'^(?P<last_name>[\w-]+)/$', views.ProfileDetailView.as_view(), name='detail'),
]