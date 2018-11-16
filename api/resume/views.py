from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from resume.models import Summary
from resume.models import Degree
from resume.models import Keys
from resume.serializers import SummarySerializer
from resume.serializers import DegreeSerializer
from resume.serializers import KeysSerializer
from rest_framework import authentication

@csrf_exempt
def summary_list(request):
    """
    List all summary
    """
    if request.method == 'GET':
        summary = Summary.objects.first()
        serializer = SummarySerializer(summary, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            summary = Summary.objects.first()
            data = JSONParser().parse(request)
            serializer = SummarySerializer(summary,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)

@csrf_exempt
def degree_list(request):
    """
    List all degrees
    """
    if request.method == 'GET':
        degree = Degree.objects.all()
        serializer = DegreeSerializer(degree, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = DegreeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
