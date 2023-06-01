from rest_framework import serializers

from places.models import Place, Image


class LoadPlaceSerializer(serializers.ModelSerializer):
    coordinates = serializers.DictField()

    class Meta:
        model = Place
        fields = ['title', 'description_short', 'description_long', 'lat', 'lng', 'coordinates']

    def is_valid(self, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        places = Place.objects.get_or_create(
            title=self.instance.get('title'),
            description_short=self.instance.get('description_short'),
            description_long=self.instance.get('description_long'),
            lat=self.instance['coordinates'].get('lat'),
            lng=self.instance['coordinates'].get('lng'))
        return places
