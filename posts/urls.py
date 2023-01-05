from django.urls import path, include

from posts.views import PostDetail, PostList

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    path("api-auth/", include('rest_framework.urls')),
]
