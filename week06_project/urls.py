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
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import *
from myapp import views as core_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^auth/', include('wl_auth.urls', namespace="wl_auth")),
    # url(r'^$', views.home, name='home'),
    # url(r'^home/', views.home, name='home'),
    url(r'^category/', views.category, name='category'),

    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', logout_page),
    # url(r'^logout/$', auth_views.login, name='login'),
    url(r'^auth/signin/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),

    url(r'^activitylist/', views.activitylist, name='activitylist'),
    url(r'^art/', views.art, name='art'),
    url(r'^camp/', views.camp, name='camp'),
    url(r'^club/', views.club, name='club'),
    url(r'^education/', views.education, name='education'),
    url(r'^music/', views.music, name='music'),
    url(r'^other/', views.other, name='other'),
    url(r'^sport/', views.sport, name='sport'),
    url(r'^workshop/', views.workshop, name='workshop'),

    url(r'^add/$', views.CreateAddView.as_view(), name='add'),
    url(r'^add/(?P<pk>[0-9]+)$', views.UpdateAddView.as_view()),
    url(r'^add_list/$', views.ListAddView.as_view(), name='add_list'),
    url(r'^detail/(?P<id>[0-9]+)$', views.detail, name="detail"),

    url(r'^vote_score/(?P<id>[0-9]+)$', views.voteScore,name = "vote_score"),
    url(r'^vote_result/(?P<id>[0-9]+)$', views.voteResult, name="vote_result"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)