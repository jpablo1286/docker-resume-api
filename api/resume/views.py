from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from resume.models import Summary
from resume.models import Degree
from resume.models import Keys
from resume.models import Certifications
from resume.models import Skill
from resume.models import Language
from resume.models import Award
from resume.models import Project
from resume.models import Expirience
from resume.models import Code
from resume.serializers import SummarySerializer
from resume.serializers import DegreeSerializer
from resume.serializers import KeysSerializer
from resume.serializers import CertificationsSerializer
from resume.serializers import SkillSerializer
from resume.serializers import LanguageSerializer
from resume.serializers import AwardSerializer
from resume.serializers import ProjectSerializer
from resume.serializers import ExpirienceSerializer
from resume.serializers import CodeSerializer
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

@csrf_exempt
def certificate_list(request):
    """
    List all certificates
    """
    if request.method == 'GET':
        certificates = Certifications.objects.all()
        serializer = CertificationsSerializer(certificates, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = CertificationsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
@csrf_exempt
def certificate_details(request, name):

    key = Keys.objects.first()
    if request.META.get('HTTP_X_APIKEY') != key.key:
        return JsonResponse({"Error" : "No valid token"}, status=400)

    try:
        certificate = Certifications.objects.get(name=name)
    except Certifications.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CertificationsSerializer(certificate)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CertificationsSerializer(certificate, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        certificate.delete()
        return HttpResponse(status=204)

@csrf_exempt
def skill_list(request):
    """
    List all skills
    """
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = SkillSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
@csrf_exempt
def skill_details(request, name):

    key = Keys.objects.first()
    if request.META.get('HTTP_X_APIKEY') != key.key:
        return JsonResponse({"Error" : "No valid token"}, status=400)

    try:
        skill = Skill.objects.get(name=name)
    except Skill.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkillSerializer(skill, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        skill.delete()
        return HttpResponse(status=204)

@csrf_exempt
def language_list(request):
    """
    List all languages
    """
    if request.method == 'GET':
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = LanguageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
@csrf_exempt
def language_details(request, name):

    key = Keys.objects.first()
    if request.META.get('HTTP_X_APIKEY') != key.key:
        return JsonResponse({"Error" : "No valid token"}, status=400)

    try:
        language = Language.objects.get(name=name)
    except Language.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(language, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        language.delete()
        return HttpResponse(status=204)

@csrf_exempt
def award_list(request):
    """
    List all awards
    """
    if request.method == 'GET':
        awards = Award.objects.all()
        serializer = AwardSerializer(awards, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = AwardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
@csrf_exempt
def award_details(request, name):

    key = Keys.objects.first()
    if request.META.get('HTTP_X_APIKEY') != key.key:
        return JsonResponse({"Error" : "No valid token"}, status=400)

    try:
        award = Award.objects.get(name=name)
    except Award.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AwardSerializer(language)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AwardSerializer(award, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        award.delete()
        return HttpResponse(status=204)

@csrf_exempt
def expirience_list(request):
    """
    List all expirience
    """
    if request.method == 'GET':
        expiriences = Expirience.objects.all()
        serializer = ExpirienceSerializer(expiriences, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        key = Keys.objects.first()
        if request.META.get('HTTP_X_APIKEY') == key.key:
            data = JSONParser().parse(request)
            serializer = ExpirienceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            print(request.META)
            return JsonResponse({"Error" : "No valid token"}, status=400)
@csrf_exempt
def expirience_details(request, name):

    key = Keys.objects.first()
    if request.META.get('HTTP_X_APIKEY') != key.key:
        return JsonResponse({"Error" : "No valid token"}, status=400)

    try:
        expirience = Expirience.objects.get(name=name)
    except Expirience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExpirienceSerializer(expirience)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExpirienceSerializer(expirience, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        expirience.delete()
        return HttpResponse(status=204)
