
from django.contrib import admin
from django.urls import path
from django.urls import include # для обращения к приложению
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')) # отслеживание главной страницы, при переходе на главную страницу '',
                                   # мы делегируем права приложению main а внутри него уже используем файл main.url

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
