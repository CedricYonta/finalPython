
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()

router.register(r'Capteur', views.CapteurViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('res', views.addrecord),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
