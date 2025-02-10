from django.urls import path
from .views import index, ImageViewSet

urlpatterns = [
    path('index/', index, name='index'),
    path('images/', ImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='images'),
]