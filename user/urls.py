from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (ProfileListApi, ProfileViewSet, ProfileDeleteApiView, ProfileDetailApiView, ProfileUpdateApiView,
                    PostListCreateApiView, PostDetailApiView, PostUpdateDeleteApiView)

# router = SimpleRouter()
# router.register('books', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', ProfileListApi.as_view()),
    path('profile/<int:pk>', ProfileDetailApiView.as_view()),
    path('profile/<int:pk>/update/', ProfileUpdateApiView.as_view()),
    path('profile/<int:pk>/delete/', ProfileDeleteApiView.as_view()),
    # posts
    path('post/', PostListCreateApiView.as_view()),
    path('post/detail/', PostDetailApiView.as_view()),
    path('postupdatedelete/<int:pk>/', PostUpdateDeleteApiView.as_view()),
]

# urlpatterns = urlpatterns + router.urls