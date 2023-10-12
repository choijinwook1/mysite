from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from pybo.views import base_views
from pybo.views import kiwon_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('kiwon/', kiwon_views.kiwon, name='kiwon'),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media 경로 추가
