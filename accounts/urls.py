from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

url_name = "accounts"
urlpatterns = [
    path("", views.UserList.as_view(), name="user_list"),
    path("<int:pk>/", views.UserDetail.as_view(), name="user_detail"),
    path("login/", views.UserLogin.as_view(), name="user_login"),
    path("logout/", views.UserLogout.as_view(), name="user_logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("emailauth/<str:token>/", views.ActivateAccountView.as_view(), name="activate-account"),
]
