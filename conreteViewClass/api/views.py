import imp
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView



class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    
# Combine of two functions (Get&Create)

class StudentLSCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    
    
# CRUD MODEL :-
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    
    
    
    
    