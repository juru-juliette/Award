from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^post$', views.post, name='post'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
]
## this references the location to the uploaded files.
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)