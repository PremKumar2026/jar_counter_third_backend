from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JarCountViewSet, third_update_jar_count

router = DefaultRouter()
router.register(r'jarcounts', JarCountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('third_update_jar_count/', third_update_jar_count, name='third_update_jar_count'),
]
