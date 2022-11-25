from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
    # Particular classes apply at authentications    
    authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    permission_classes=[IsAdminUser] # this is only work where  staff_status  is true
