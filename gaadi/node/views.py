from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from .models import controlCommand
from rest_framework.views import APIView

class controlCommandView(APIView):
    def get(self,request):
         data=controlCommand.objects.all()
         return HttpResponse(data.data)
    
    
    
   
