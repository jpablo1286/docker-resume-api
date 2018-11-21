from django.contrib.auth.models import User
from rest_framework import serializers

from resume.models import Keys
from resume.models import Summary
from resume.models import Degree
from resume.models import Language
from resume.models import Certifications
from resume.models import PersonalData
from resume.models import Skill
from resume.models import Award
from resume.models import Project
from resume.models import Expirience
from resume.models import Code

class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = ('name', 'key')

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('name', 'currentPosition','summary')

class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ('fieldName', 'fieldValue')

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ('name', 'institution','degree','date')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'written','reading','spoken')

class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = ('name', 'institution','date')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description')

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('name', 'description','institution','date')

class ExpirienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expirience
        fields = ('name','institution','description','date')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','institution','description','date')

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('name','url','description')
