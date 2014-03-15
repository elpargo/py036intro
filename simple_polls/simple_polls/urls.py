from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'simple_polls.views.hello', name='home'),
    url(r'^environ$', 'simple_polls.views.environ'),
    url(r'^environ_with_template$', 'simple_polls.views.environ_with_template'),
    url(r'^(\w+)$', 'simple_polls.views.hello_name', name='hello_name'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
