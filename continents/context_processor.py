
from continents.models import Continent


def countinents_data(request):
    continents = Continent.objects.all()
    return {'continents': continents}