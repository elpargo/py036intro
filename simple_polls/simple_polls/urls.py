from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from  simple_polls.views import SurveyCreate

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'simple_polls.views.hello', name='home'),
    url(r'^environ$', 'simple_polls.views.environ'),
    url(r'^environ_with_template$', 'simple_polls.views.environ_with_template'),
    url(r'^survey/add$', SurveyCreate.as_view()),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
