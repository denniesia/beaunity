from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from beaunity.accounts.api_views import (AppUserRegisterAPIView, LoginAPIView,
                                         LogoutAPIView)

urlpatterns = [
    path('register/', AppUserRegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='api-login'),
    path('logout/', LogoutAPIView.as_view(), name='api-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),
]

