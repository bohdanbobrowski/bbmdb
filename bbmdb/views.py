from django.http import HttpResponse
from rest_framework import generics
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentsSerializer
import json
import omdb

API_KEY='95667d5d'
omdb.set_default('apikey', API_KEY)


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            movie = Movies.objects.get(title=request.data.title)
        except Movies.DoesNotExist:
            movie = {}
        return movie


class CommentsListView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class MovieCommentsView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TopView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

