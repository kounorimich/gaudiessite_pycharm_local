from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Live

# Create your views here.
class LiveIndexView(TemplateView):
    template_name = 'lives_index.html'

    def get_context_data(self, **kwargs):
        context = super(LiveIndexView, self).get_context_data(**kwargs)
        context['lives'] = Live.objects.all()
        return context


index = LiveIndexView.as_view()
