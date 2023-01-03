from django.urls import path, include
from .views import (
    UserChangePasswordView, student_api_view, StudentApiView, CustomAuthStudentApiView, 
    CustomUserRegistrationView, CustomUserLoginView, UserProfileView,
    UserChangePasswordView, UserSendResetPasswordEmailView, UserPasswordResetConfirmView
)
from rest_framework.routers import DefaultRouter
from .custom_auth_token import CustomAuthToken

app_name = "restAuthApi"

router5 = DefaultRouter()
router5.register('token_auth', StudentApiView, basename="token-authentication") # use built in token authentication class

router5.register('custom_token_auth', CustomAuthStudentApiView, basename="custom-token-authentication") # user custom authentication class

urlpatterns = [

    path('student/', student_api_view, name="student-api-view-list"),
    path('<int:pk>/', student_api_view, name="student-api-view-detail"),
    path('custom_token_generate/', CustomAuthToken.as_view()),
    path('custom_user_registration/', CustomUserRegistrationView.as_view(), name="custom-user-registration"),
    path('custom_user_login/', CustomUserLoginView.as_view(), name="custom-user-login"),
    path('user_profile/', UserProfileView.as_view(), name="user-profile"),
    path('changepassword/', UserChangePasswordView.as_view(), name="changepassword"),
    path('password_reset_email/', UserSendResetPasswordEmailView.as_view(), name="password-reset-email"),
    path('password_reset_confirm/<uid>/<token>/', UserPasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path('', include(router5.urls))
]