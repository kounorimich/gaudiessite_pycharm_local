import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Live

# Create your views here.
class LiveIndexView(TemplateView):
    template_name = 'lives_index.html'

    def get_context_data(self, **kwargs):
        context = super(LiveIndexView, self).get_context_data(**kwargs)
        # context['lives'] = Live.objects.all()
        future_lives = Live.objects.filter(date__gte=datetime.datetime.today())
        past_lives = Live.objects.filter(date__lt=datetime.datetime.today())
        past_lives_ordered = past_lives.order_by("-date")
        context["future_lives"] = future_lives
        context["past_lives_ordered"] = past_lives_ordered

        return context



index = LiveIndexView.as_view()
