"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )

from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import user_passes_test

anonymous_required =  user_passes_test(
    lambda user: user.is_anonymous(),
    settings.LOGIN_REDIRECT_URL,
    redirect_field_name = 'next')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^grades/', include('grade.urls', namespace='grade')),
    url(r'^subject/', include('subject.urls', namespace='subject')),
    url(r'^professor/', include('professor.urls', namespace='professor')),
    url(r'^user/', include('user.urls', namespace='user')),
]
