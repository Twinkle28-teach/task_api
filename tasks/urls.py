from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import TaskViewSet, MeView

urlpatterns = router.urls + [
    path("me/", MeView.as_view()),
]
