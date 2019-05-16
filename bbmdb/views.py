from rest_framework import generics
from .models import Movie, Comment
from .serializers import MoviesSerializer, CommentsSerializer


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

class CommentsListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class MovieCommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class TopView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

