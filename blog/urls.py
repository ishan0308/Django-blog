from django.urls import include,re_path
from blog.views import archive,create_blogpost,display_blogs
urlpatterns = [
    re_path(r'^$', archive, name='archive'),
    re_path(r'^create/', create_blogpost, name='create_blogpost'),
    re_path(r'^display/', display_blogs, name='display_blogs'),
]