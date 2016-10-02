from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_name.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='HomePage'),
)
