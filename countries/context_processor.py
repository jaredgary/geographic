from django.urls import reverse
from countries.models import Country


def countries_data(request):
    countries = Country.objects.all()
    return {'countries': countries}