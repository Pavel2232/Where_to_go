from urllib.parse import urlparse
import requests
from django.core.management import BaseCommand
from places.models import Place, Image
from places.serializers import LoadPlaceSerializer
from django.core.files.base import ContentFile


def get_name_image_by_url(url: str) -> str:
    url_path = urlparse(url).path
    result = url_path.split('/')
    return result[-1]


class Command(BaseCommand):
    help = """Загрузка данных на сервер, формат:http://адрес/файла.json, для картинки так же -img и ссылка.
     Важно! фотография прикрепитсья автоматически к последней добавленной place"""

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
                    name_img = get_name_image_by_url(image_url)
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
