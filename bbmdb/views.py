from rest_framework import generics
from .models import Movies
from .serializers import MoviesSerializer


class MoviesView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
        """handle post request here"""
        pass

class CommentsView(generics.RetrieveAPIView):
    pass


class TopView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer