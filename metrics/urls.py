from django.conf.urls import patterns, url

# Temporary stub view
urlpatterns = patterns('metrics.views',
    url(r'^metrics/$', 'query_metrics'),
)