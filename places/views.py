from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from places.models import Place


# Create your views here.
@csrf_exempt
def index(request):
    places = Place.objects.all()
    response = []
    for place in places:
        response.append({
            'id': place.id,
            'title': place.title,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': [place.lng, place.lat],
            'image': place.image
        })
    return (render(request,'index.html', context = {'response':response}))