
from django.conf.urls import url
from django.contrib import admin

from streamingproject import views

# url patterns for browsing 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stream/(?P<num>\d+)/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="dynamic_stream"),  
    url(r'^stream/screen/$',views.indexscreen),
]
