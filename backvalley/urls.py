from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'startups', views.StartupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'sectors', views.SectorViewSet)
router.register(r'roles', views.RoleViewSet)

urlpatterns = [
    path("", include(router.urls))
]