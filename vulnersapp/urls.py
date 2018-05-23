from django.conf.urls import include, url
from django.contrib import admin
from main.views import index, save_file

urlpatterns = [
    # Examples:
    # url(r'^$', 'vulners.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^save/', save_file, name='save_file'),
    url(r'^admin/', include(admin.site.urls)),
]
