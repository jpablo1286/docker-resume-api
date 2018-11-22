from django.urls import path
from resume import views

urlpatterns = [
    path('summary/', views.summary_list),
    path('degree/', views.degree_list),
    path('certificate/', views.certificate_list),
    path('certificate/<str:name>', views.certificate_details),
    path('skill/', views.skill_list),
    path('skill/<str:name>', views.skill_details),
    path('language/', views.language_list),
    path('language/<str:name>', views.language_details),
    path('award/', views.award_list),
    path('award/<str:name>', views.award_details),
    path('expirience/', views.expirience_list),
    path('expirience/<str:name>', views.expirience_details),
    path('project/', views.project_list),
    path('project/<str:name>', views.project_details),
    path('code/', views.code_list),
    path('code/<str:name>', views.code_details),
    path('personaldata/', views.personaldata_list),
    path('personaldata/<str:name>', views.personaldata_details)
]
