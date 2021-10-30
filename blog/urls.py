from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^viewpost/(?P<post_id>\d+)$', viewpost, name='viewpost'),
    url(r'^add_post/(?P<post_id>\d+)$', add_post, name='add-post'),
    url(r'^add_like/(?P<post_id>\d+)$', add_like, name='add-like'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
    # url(r'^delete_comment', delete_comment, name='delete-comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
