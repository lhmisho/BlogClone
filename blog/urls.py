from django.urls import path
from .views import *
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/details/', PostDetailView.as_view(), name='post-detial'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/drafts/list/', PostDrafListView.as_view(), name='post-draft-list'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', remove_comment, name='remove_comment'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
]