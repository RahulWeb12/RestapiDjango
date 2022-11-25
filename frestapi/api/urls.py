from django.conf.urls import url, include
from .views import student_api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^student/',student_api),
    ]
