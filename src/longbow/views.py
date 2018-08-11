from django.shortcuts import render

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from longbow.models import Test


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'longbow/index.html'

    def get_queryset(self):
        return Test.objects.all().order_by('-pub_date')

