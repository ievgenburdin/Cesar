from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.cesar_page, name='cesar_page'),
	url(r'^c/$',views.crypting),
    url(r'^d/$',views.decrypting),
	url(r'^i/$',views.info),
]+static(settings.STATIC_URL)