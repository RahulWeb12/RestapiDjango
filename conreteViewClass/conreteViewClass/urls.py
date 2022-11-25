from django import views
from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Group -1
    
    # path('studentapi/',views.StudentList.as_view()), 
    # path('studentapi/',views.StudentCreate.as_view()), 
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()), 
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()), 
    # path('studentapi/<int:pk>/',views.StudentDestroy.as_view()), 
    
    # Group -2
    # Combine of two urls in one line (GET,CREATE)
    # path('studentapi/',views.StudentLSCreate.as_view()), 
    # path('studentapi/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    
    
    # Group -3 (Complete CrudModel Created)
    path('studentapi/',views.StudentListCreate.as_view()), 
    path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    

    
]