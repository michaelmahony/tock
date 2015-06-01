from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^projects.(?P<format>csv|json)$', views.ProjectList.as_view(), name='ProjectList'),
    url(r'^users.(?P<format>csv|json)$', views.UserList.as_view(), name='UserList'),
    url(r'^timecards.(?P<format>csv|json)$', views.TimecardList.as_view(), name='TimecardList'),
    url(r'^project_timeline.csv$', views.ProjectTimelineView, name='ProjectTimelineView'),
    url(r'^user_timeline.csv$', views.UserTimelineView, name='UserTimelineView'),
)
