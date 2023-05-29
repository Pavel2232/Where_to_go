from urllib.parse import urlparse, unquote

import requests
from django.core.management import BaseCommand
from requests import JSONDecodeError

from places.models import Place, Image
from places.serializers import LoadPlaceSerializer
from django.core.files.base import ContentFile

def get_name_url(url: str)-> str:
    url_path = urlparse(url).path
    result = url_path.split('/')
    return result[-1]


class Command(BaseCommand):
    help = "Загрузка данных на сервер"

    def add_arguments(self, parser):

        parser.add_argument('requests', nargs='+', type=str)
        parser.add_argument('-img',
                            action='store_true',
                            default=False)
    def handle(self, *args, **options):
        if options.get('img'):
            try:
                for image_url in options.get('requests'):
                    request = requests.get(image_url)
                    imgs_raw = ContentFile(request.content)
                    image = Image.objects.create(places=Place.objects.all().last())
                    name_img = get_name_url(image_url)
                    image.imgs.save(name_img, imgs_raw, save=True)
            except Exception as e:
                print(f"Ошибка запроса: {e}")
        else:
            try:
                for request in options.get('requests'):
                    response = requests.get(request)
                    serializer = LoadPlaceSerializer(response.json())
                    serializer.create(response.json())
            except Exception as e:
                print(f"Ошибка запроса: {e}")


