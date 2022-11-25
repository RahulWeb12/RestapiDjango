import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello(request):
#     return Response({'msg': 'hello'})

        # Or 
# @api_view(['GET'])
# def hello(request):
#     return Response({'msg': 'hello'})


# @api_view(['POST'])
# def hello(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg': 'This is POST Request'})


@api_view(['GET','POST'])
def hello(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg': 'This is GET Request'})
    
    
    if request.method=='POST':
        print(request.data)
        return Response({'msg': 'This is POST Request'})
