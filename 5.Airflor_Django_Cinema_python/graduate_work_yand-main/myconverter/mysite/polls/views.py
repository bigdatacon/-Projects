from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import FilmWork, Fileupl
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FileuplSerializer, FilmWorkSerializer

class FileuplViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fileupl.objects.all()
    serializer_class = FileuplSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FilmWorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FilmWork.objects.all()
    serializer_class = FilmWorkSerializer
    # permission_classes = [permissions.IsAuthenticated]


def index(request):
    data = []
    for film in FilmWork.objects.all():
        film_info = {
            'uuid': film.id,
            'title': film.title,
            'certificate': film.certificate,
            'file_path': film.file_path.url,
            'files': []
        }
        for furl in film.files.all():
            film_info['files'].append(furl.file_path.url)
        data.append(film_info)
    return JsonResponse({'results': data})