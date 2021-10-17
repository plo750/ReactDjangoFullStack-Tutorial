from django.urls import path, include
from . import views
#from .views import Another, BookViewSet
from .views import BookViewSet
from rest_framework import routers

# serializers
router = routers.DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('first', views.first),
    #path('another', Another.as_view()),
    path('showTemplate', views.show_template),
    path('', include(router.urls))
]


