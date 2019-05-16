from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentsSerializer


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            movie = Movies.objects.get(title=request.data['title'])
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Movies.DoesNotExist:
            return self.create(request, *args, **kwargs)


class CommentsListView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class MovieCommentsView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TopView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

