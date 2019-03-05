from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # landing page
    url('^$', views.photos, name='photos'),
    # search results page
    url(r'^search/', views.search_results, name='search_results'),
    url(r"^page/",views.page, name = "location"),
    url(r"^location/(\w+)",views.location, name = "locations")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
