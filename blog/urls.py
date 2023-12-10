from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post_list'),
    path('create/', BlogPostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),
]
