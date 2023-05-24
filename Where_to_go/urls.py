from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from Where_to_go import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

