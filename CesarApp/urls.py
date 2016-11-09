from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.cesar_page, name='cesar_page'),
	url(r'^data/$',views.crypting),
	url(r'^info/$',views.info),
]+static(settings.STATIC_URL)