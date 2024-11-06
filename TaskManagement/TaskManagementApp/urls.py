from django.urls import path
from .views import UserRegistration,Tasks,TaskDetails
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/', UserRegistration.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('task/', Tasks.as_view()),
    path('task/<task_id>', TaskDetails.as_view()),

  
]