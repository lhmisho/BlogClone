from django.urls import path
from .views import *
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/details/', PostDetailView.as_view(), name='post-detial'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/drafts/list/', PostDrafListView.as_view(), name='post-draft/list'),
]