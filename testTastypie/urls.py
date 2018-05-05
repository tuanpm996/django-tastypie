from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from actions.resources import *
# from actions.resources import ActionResource

v1_api = Api(api_name='v1')
v1_api.register(ActionResource())
v1_api.register(ActionTypeResource())
v1_api.register(DealActionResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'testTastypie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tuanpm/api/', include(v1_api.urls)),
    url(r'^tuanpm/actions/', include('actions.urls')),
]
