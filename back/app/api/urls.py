from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('molecule/list/', views.moleculeList),
    path('activity/list/', views.activitiesList),
    path('molecule/<str:pk>/', views.molecule),
    path('molecule/<str:pk>/activities/', views.moleculeActivities),
]