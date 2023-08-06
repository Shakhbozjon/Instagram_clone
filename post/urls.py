from django.urls import path
from .views import (
    PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView, PostCreateForm, like
)


urlpatterns = [
    # path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list'),
    # path('<uuid:post_id>', PostDetail, name='post-details'),
    path('<uuid:post_id>/like', like, name='like'),
]
