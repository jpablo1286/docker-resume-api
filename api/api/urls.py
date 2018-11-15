from django.urls import path
from resume import views

urlpatterns = [
    path('summary/', views.summary_list)
]
