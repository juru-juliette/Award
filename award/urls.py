from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^post$', views.post, name='post'),
    url(r'^accounts/profile/(\d+)', views.profile, name='profile'),
    url(r'^accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profile'),
    url(r'^api/project/$', views.ProjectList.as_view(),name='project'),
    url(r'^grade/(\d+)',views.grade_project,name ='grade') ,
]
## this references the location to the uploaded files.
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)