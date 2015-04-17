from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import registration.backends.default.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matchmaker.views.home', name='home'),
    # url(r'^matchmaker/', include('matchmaker.foo.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{
    'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
    'document_root': settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'profiles.views.all', name='home'),
    url(r'^members/(?P<username>\w+)/$', 'profiles.views.single_user', name='members'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(registration.backends.default.urls)),
    url(r'^edit/$', 'profiles.views.edit_profile', name='edit_profile'),
    url(r'^questions/$', 'questions.views.all_questions', name='questions'),
    (r'^edit/jobs$', 'profiles.views.edit_jobs'),
    (r'^edit/locations$', 'profiles.views.edit_locations'),
)
