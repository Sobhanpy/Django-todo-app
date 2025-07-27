from django.urls import path, include
from todo.api.V1.views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('tasks', TaskViews, basename='Tasks')

urlpatterns = router.urls
