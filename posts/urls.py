from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename="users")
router.register('', PostViewSet, basename="posts")

urlpatterns = router.urls
