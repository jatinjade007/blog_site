from django.urls import path
from blog.views import *

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blogs')
    
    path('addblog/', CreateBlog.as_view(), name='blog__create')

    path('blog/blog_content/', BlogContentAddUpdate.as_view(), name='blog_content_add_update')

    path('blog/comments', CommentView.as_view(), name='comments')
]