from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewList

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewList, basename="posts")

urlpatterns = router.urls
