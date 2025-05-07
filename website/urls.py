from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/', User.as_view(), name='usuarios'),
    path('api/user/<int:id>', User.as_view(), name="usuarioDetalhe"),
    

                      
               
]