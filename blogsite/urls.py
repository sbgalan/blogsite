from django.conf.urls import include, url
from django.urls import path, reverse_lazy
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(('blog.urls', 'blog'), namespace="blog")),
]
