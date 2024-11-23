from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import token auth view
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)  # Register the Booking viewset

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),  # Token auth
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),  # Include the router urls for bookings
]
