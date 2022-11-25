from django import views
from django.contrib import admin
from django.urls import path
from api import views

# Direct urls call....
 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('studentapi/',views.student_api),
#     path('studentapi/<int:pk>',views.student_api),
# ]

from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/',include('api.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)