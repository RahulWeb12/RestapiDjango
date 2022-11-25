from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    # Particular classes apply at authentications    
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser] # this is only work where  staff_status  is true
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissions]