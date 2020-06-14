from rest_framework import routers
from .views import UserViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todo', TodoViewSet)

urlpatterns = router.urls
