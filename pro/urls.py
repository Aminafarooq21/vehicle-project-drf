"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('owner/<int:pk>', views.OwnerAPIWithId.as_view(),name='owner_with_id'),
    path('owner/', views.OwnerApiWithoutId.as_view(), name='owner_without_id'),

    path('car/<int:pk>', views.CarAPIWithId.as_view(),name='car_with_id'),
    path('car/', views.CarApiWithoutId.as_view(), name='car_without_id'),

    path('bus/<int:pk>', views.BusAPIWithId.as_view(), name='bus_with_id'),
    path('bus/', views.BusApiWithoutId.as_view(), name='bus_without_id'),

    path('bike/<int:pk>', views.BikeAPIWithId.as_view(), name='bike_with_id'),
    path('bike/', views.BikeApiWithoutId.as_view(), name='bike_without_id'),

    path('vehicle/<int:pk>', views.VehicleAPIWithId.as_view(), name='vehicle_with_id'),
    path('vehicle/', views.VehicleApiWithoutId.as_view(), name='vehicle_without_id'),
    path('gettoken/', TokenObtainPairView.as_view(),name='token'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify')

]
