from django.urls import path

from auth_app.views import CreateUserView

urlpatterns = [
    path('sign-in/', CreateUserView.as_view(), name='sign-in'),
]
