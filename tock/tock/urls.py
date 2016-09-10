from django.conf import settings
from django.conf.urls import include, url

# Enable the Django admin.
from django.contrib import admin
admin.autodiscover()

import hours.views
import api.urls
import projects.urls
from . import views

urlpatterns = [
    url(r'^$',
        hours.views.ReportingPeriodListView.as_view(),
        name='ListReportingPeriods'
    ),
    url(r'^callback$',
        views.oauth2_callback,
        name='callback'
    ),
    url(r'^login$',
        views.login,
        name='login'
    ),
    url(r'^logout$',
        views.logout,
        name='logout'
    ),
    url(r'^reporting_period/', include(
        'hours.urls.timesheets',
        namespace='reportingperiod'
    )),
    url(r'^reports/', include(
        'hours.urls.reports',
        namespace='reports'
    )),
    url(r'^employees/', include(
        'employees.urls',
        namespace='employees'
    )),
    url(r'^projects/', include(projects.urls)),

    # TODO: version the API?
    url(r'^api/', include(api.urls)),

    # Enable the Django admin.
    url(r'^admin/', include(admin.site.urls)),
]


# Enable Django Debug Toolbar only if in DEBUG mode.
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
