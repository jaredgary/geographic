# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from people.models import Person


# Create your views here.
from people.forms import RegisterFormModel


def register(request):
    fathers = Person.objects.filter(children__isnull=True)
    form = RegisterFormModel(fathers, request.POST or None)

    if form.is_valid():
        person = form.save()
        return JsonResponse({
            'name': person.first_name,
            'father': str(person.father),
            'nacionality': ','.join([
                str(country) for country in person.nacionality.all()
            ])
        })

    return render(request, "people/register.html", {'form': form})

