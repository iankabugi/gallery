from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    # landing page
    url('^$', views.photos, name='photos'),
    # search results page
    url(r'^search/', views.search_results, name='search_results'),
    # link to the image details
    url(r'^image/(\d+)', views.image, name='image')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
