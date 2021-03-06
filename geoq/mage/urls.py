from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from views import mage_login, get_events, get_observations, get_icon, get_attachment


urlpatterns = patterns('',
    url(r'^api/events/?$', get_events, name='get-events'),
    url(r'^api/events/(?P<id>\d+)/observations/?$', get_observations, name='get-observations'),
    url(r'^api/events/(?P<id>\d+)/form/icons/(?P<type>[ \S]+)/?$', get_icon, name='get-icon'),
    url(r'^api/events/(?P<id>\d+)/observations/(?P<obs>\S+)/attachments/(?P<att>\S+)/?$', get_attachment, name='get-attachment'),
)
