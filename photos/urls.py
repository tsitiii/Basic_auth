from django.urls import path
from .views import index, ImageViewSet, home

urlpatterns = [
    path('index/', index, name='index'),
    path('', home,name='home'),
    path('images/', ImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='images'),
]