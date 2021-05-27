from django.views import generic

from gist_app.models import Gist


class IndexGistView(generic.ListView):
    queryset = Gist.objects.all()
    template_name = 'index.html'
