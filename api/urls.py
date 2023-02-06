from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CSVDataViewSet
from . import views

router = SimpleRouter()
router.register(r'upload', CSVDataViewSet)

urlpatterns = router.urls

