from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Talks.models import Talks
from Talks.serializers import TalksSerializer

# Create your views here.

@csrf_exempt
def AllTalks(request):
  if request.method=='GET':
      talks = Talks.objects.all()
      talks_serializer=TalksSerializer(talks,many=True)
      return JsonResponse(talks_serializer.data,safe=False)

def GetTalksById(request, id):
  if request.method=='GET':
    talk = Talks.objects.get(talk_id=id)
    talk_serializer=TalksSerializer(talk)
    return JsonResponse(talk_serializer.data,safe=False)


