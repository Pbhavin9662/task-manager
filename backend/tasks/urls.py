from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register('', TaskViewSet,basename="task_view_set")
urlpatterns = router.urls
