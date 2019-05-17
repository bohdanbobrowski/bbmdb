from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentsSerializer, TopMoviesSerializer


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
        try:
            movie = Movies.objects.get(title=request.data['title'])
            serializer = self.get_serializer(movie)
            return Response(serializer.data)
        except Movies.DoesNotExist:
            return self.create(request, *args, **kwargs)


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        if 'movie_id' in self.kwargs:
            return Comments.objects.filter(movie_id=self.kwargs['movie_id'])
        else:
            return Comments.objects.all()


class TopListView(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = TopMoviesSerializer

    def get_queryset(self):
        return Movies.objects.filter()\
            .annotate(comments_count=Count('comments'))\
            .order_by('-comments_count')
