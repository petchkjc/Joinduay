"""week06_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('wl_auth.urls', namespace="wl_auth")),
    url(r'^home/', views.home, name='home'),
    url(r'^add_poll/$', views.CreateAddView.as_view(), name='add_poll'),
    url(r'^add_poll/(?P<pk>[0-9]+)$', views.UpdateAddView.as_view()),
    url(r'^add_poll_list/$', views.ListAddView.as_view(), name='add_poll_list'),
    url(r'^vote/', views.Vote, name='vote'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)