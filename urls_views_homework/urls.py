"""urls_views_homework URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from family_app.views import index_view, poston_view, paasch_view, jacobs_view, kesgen_view, poston_parents_view
from family_app.views import poston_kids_view, poston_kids_career_view
from family_app.views import paasch_thelanding_view, paasch_activities_view, paasch_latest_projects_view
from family_app.views import jacobs_activities_view, kesgen_activities_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^poston$', poston_view),
    url(r'^poston/parents$', poston_parents_view),
    url(r'^poston/kids$', poston_kids_view),
    url(r'^poston/kids/careers$', poston_kids_career_view),
    url(r'^paasch$', paasch_view),
    url(r'^paasch/thelanding$', paasch_thelanding_view),
    url(r'^paasch/thelanding/activities$', paasch_activities_view),
    url(r'^paasch/thelanding/activities/latest_projects$', paasch_latest_projects_view),
    url(r'^jacobs$', jacobs_view),
    url(r'^jacobs/activities$', jacobs_activities_view),
    url(r'^kesgen$', kesgen_view),
    url(r'^kesgen/activities$', kesgen_activities_view),

]
