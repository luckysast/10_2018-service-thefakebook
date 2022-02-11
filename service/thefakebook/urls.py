"""thefakebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.urls import path
from django.views.generic import RedirectView

from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^profile$', profile),
    url(r'^profile/(?P<profile_id>\d{1,50})$', profile),
    url(r'^profile/edit$', profile_edit),
    url(r'^profile/pic_edit$', picture_edit),
    url(r'^search$', search_result),
    url(r'^index$', index),
    url(r'^schools_supported$', schools_supported),
    url(r'^contact_us$', contact_us),
    url(r'^terms_of_use$', terms_of_use),
    url(r'^register$', register),
    url(r'^login$', signin),
    url(r'^logout$', signout),
    url(r'^profile/(?P<profile_id>\d{1,50})/add_to_friend$', add_friend),
    url(r'^profile/(?P<profile_id>\d{1,50})/remove_from_friend$', remove_friend),
    url(r'^friends$', friends),
    url(r'^friends/requests$', friends_requests),
    url(r'^messages$', all_messages),
    url(r'^messages/(?P<profile_id>\d{1,50})$', messages_view),
    url(r'^$', RedirectView.as_view(url='index')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': "core/static"}),
]
