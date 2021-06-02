from django.urls import path

from auth_app.views import CreateUserView

urlpatterns = [
    path('sign-up/', CreateUserView.as_view(), name='sign-up'),
]
