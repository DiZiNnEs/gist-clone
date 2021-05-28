from django.views import generic

from gist_app.models import Gist


class IndexGistView(generic.ListView):
    queryset = Gist.objects.all()
    template_name = 'index.html'


class GistDetailView(generic.DetailView):
    queryset = Gist.objects.all()
    template_name = 'detail-gist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('object').slug
        context['detail_object'] = self.queryset.filter(slug=slug)
        return context
