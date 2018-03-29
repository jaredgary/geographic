# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views.generic import TemplateView


class ContinentsView(TemplateView):
    template_name = 'continents/continents.html'