import copy

from django.shortcuts import render
from django.urls import reverse

from places.models import Place, Image
from django.http import JsonResponse



def index(request):
    features = []
    feature_template = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {
            "title": "title",
            "placeId": "placeId",
            "detailsUrl": "detailsUrl",
        },
    }

    places = Place.objects.all()

    for place in places:
        new_feature = copy.deepcopy(feature_template)
        new_feature["geometry"]["coordinates"][0] = place.lng
        new_feature["geometry"]["coordinates"][1] = place.lat
        new_feature["properties"]["title"] = place.title
        new_feature["properties"]["placeId"] = "placeId" + str(place.id)
        new_feature["properties"]["detailsUrl"] = reverse(
            "detail_view", kwargs={"pk": place.id}
        )
        features.append(new_feature)

    places_data = {"type": "FeatureCollection", "features": features}
    context = {"places_data": places_data}
    return render(request, "index.html", context)



def detail_view(request, pk):
    place = Place.objects.get(pk=pk)

    response = {
        'title': place.title,
        'imgs': [],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    imgs = Image.objects.filter(places=place.id)
    for image in imgs:
        response['imgs'].append(image.imgs.url)

    return JsonResponse(response)
