from django.shortcuts import render,HttpResponseRedirect
from .forms import information
 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import info
from.serializers import infoSerializer

# Create your views here.


# this function for add new items and show items
def index(request):
    return render(request, 'myapp/index.html')





def add(request):
    
    if request.method == 'POST':                  # here if we post the request or request is post after submitting
      fm = information(request.POST)       #the fm a object were all data come from form (studentregistration)
      if fm.is_valid():#validation of the data
        fm.save()#save our data
        fm = information( )  #shows us a blank form after adding data
    else:
        fm = information()
    
               
    return render(request, 'myapp/add.html',{'form':fm})

def show(request):
    student = info.objects.all()
    return render(request, 'myapp/show.html',{'stu':student})   



class infolist (APIView):
    def get(self,request):
        info1=info.objects.all()
        serializer=infoSerializer(info1,many=True)
        return Response(serializer.data)
    
    # def post(self,request):  #for post the data into database
    #     serializer=infoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    
    