from rest_framework import generics
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentsSerializer


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class CommentsListView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class MovieCommentsView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TopView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

