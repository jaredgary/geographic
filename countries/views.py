# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView

from countries.forms import CountryCreateFormModel
from countries.models import Country


class HomeView(TemplateView):
    template_name = 'countries/home.html'


class TagsView(TemplateView):
    template_name = 'countries/tags.html'


class CountryDetailView(TemplateView):
    template_name = 'countries/country_detail.html'

    def get_context_data(self, **kwargs):
        code = kwargs['code']
        return {'code': code}


class CountryDetailIdView(DetailView):
    template_name = 'countries/country_id_detail.html'
    model = Country


class CountrySearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        query = self.kwargs['query']
        return Country.objects.filter(name__contains=query)


class CreateCountryView(TemplateView):
    template_name = 'countries/register.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = CountryCreateFormModel(request.POST or None)
        return super(CreateCountryView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return {'form': self.form}

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            country = self.form.save()
            return JsonResponse({
                "name": country.name
            })

        return self.get(request, *args, **kwargs)