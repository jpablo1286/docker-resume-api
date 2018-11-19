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
    path('language/<str:name>', views.language_details)
]
