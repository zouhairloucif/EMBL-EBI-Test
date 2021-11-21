from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MoleculeSerializer, ActivitySerializer
from .models import Molecule, Activity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

"""
API Overview
"""


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Molecule List': '/molecule/list/',
        'Molecule': '/molecule/<str:pk>/',
        'Activities List': '/molecule/<str:pk>/activities/',
    }
    return Response(api_urls)


@api_view(['GET'])
def molecule(request, pk):
    molecules = Molecule.objects.get(pk=pk)
    serializer = MoleculeSerializer(molecules, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def moleculeList(request):
    molecules = Molecule.objects.all()
    paginator = Paginator(molecules, 12)
    page_num = request.GET.get('page')

    try:
        molecules = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        molecules = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        molecules = paginator.page(paginator.num_pages)

    serializer = MoleculeSerializer(molecules, many=True)
    return Response({'totalPages': paginator.num_pages, 'data': serializer.data})


@api_view(['GET'])
def activitiesList(request):
    activities = Activity.objects.all()
    paginator = Paginator(activities, 12)
    page_num = request.GET.get('page')

    try:
        activities = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        activities = paginator.page(paginator.num_pages)

    serializer = ActivitySerializer(activities, many=True)
    return Response({'totalPages': paginator.num_pages, 'data': serializer.data})


@api_view(['GET'])
def moleculeActivities(request, pk):
    molecules = Molecule.objects.get(pk=pk)
    activities = molecules.activities.all()
    paginator = Paginator(activities, 12)
    page_num = request.GET.get('page')

    try:
        activities = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        activities = paginator.page(paginator.num_pages)

    serializer = ActivitySerializer(activities, many=True)
    return Response({'totalPages': paginator.num_pages, 'data': serializer.data})
