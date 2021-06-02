from django.urls import path

from auth_app.views import CreateUserView, LoginUserView

urlpatterns = [
    path('sign-up/', CreateUserView.as_view(), name='sign-up'),
    path('sign-in/', LoginUserView.as_view(), name='sign-in'),
]
