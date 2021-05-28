from django.urls import path

from gist_app.views import IndexGistView, GistDetailView

urlpatterns = [
    path('', IndexGistView.as_view(), name='index-gist'),
    path('gist/<slug:slug>/', GistDetailView.as_view(), name='detail-gist'),
]
