from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Talks.models import Talks
from Talks.serializers import TalksSerializer

# Create your views here.

@csrf_exempt
def TalksApi(request, id=0):
  if request.method=='GET':
      talks = Talks.objects.all()
      talks_serializer=TalksSerializer(talks,many=True)
      return JsonResponse(talks_serializer.data,safe=False)
  elif request.method=='POST':
    talks_data=JSONParser().parse(request)
    talks_serializer=TalksSerializer(data=talks_data)
    if talks_serializer.is_valid():
      talks_serializer.save()
      return JsonResponse("Added Successfully",safe=False)
    return JsonResponse("Failed to Add",safe=False)
  elif request.method=='PUT':
    talks_data=JSONParser().parse(request)
    talks=Talks.objects.get(talk_id=talks_data['talk_id'])
    talks_serializer=TalksSerializer(talks, data=talks_data)
    if talks_serializer.is_valid():
      talks_serializer.save()
      return JsonResponse("Update Successfully",safe=False)
    return JsonResponse("Failed to Update")
  elif request.method=='DELETE':
    talk=Talks.object.get(talk_id=id)
    talk.delete()
    return JsonResponse("Deleted Successfully",safe=False)

def GetTalksById(request, id):
  if request.method=='GET':
    talk = Talks.objects.get(talk_id=id)
    talk_serializer=TalksSerializer(talk)
    return JsonResponse(talk_serializer.data,safe=False)


