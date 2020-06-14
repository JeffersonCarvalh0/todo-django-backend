from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import TodoViewSet, UserDetail, UserCreate

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += format_suffix_patterns([
    path('user/', UserDetail.as_view(), name='user-detail'),
    path('register/', UserCreate.as_view(), name='user-create'),
])

