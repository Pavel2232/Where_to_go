from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place
from django.http import JsonResponse


def index(request):
    features = []

    places = Place.objects.all()

    for place in places:
        feature_template = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]},
            'properties': {
                'title': place.title,
                'placeId': 'placeId {}'.format(str(place.id)),
                'detailsUrl': reverse('detail_view', kwargs={'pk': place.id}),
            },
        }
        features.append(feature_template)

    context = {'places_data': {
        'type': 'FeatureCollection',
        'features': features,
    }
    }
    return render(request, 'index.html', context)


def detail_view(request, pk):
    place = get_object_or_404(Place, pk=pk)
    response = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 2}, safe=False)
