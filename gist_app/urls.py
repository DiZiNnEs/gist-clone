from django.urls import path

from gist_app.views import IndexGistView

urlpatterns = [
    path('', IndexGistView.as_view(), name='index-gist'),
]
