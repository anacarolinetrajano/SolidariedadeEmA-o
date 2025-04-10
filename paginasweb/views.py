from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'


class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'