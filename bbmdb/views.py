from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movies, Comments, MoviesPagination
from .serializers import MoviesSerializer, MoviesListSerializer, CommentsSerializer, TopMoviesSerializer


class MoviesListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesListSerializer
    pagination_class = MoviesPagination

    def post(self, request, *args, **kwargs):
        try:
            movie = Movies.objects.get(title=request.data['title'])
            serializer = MoviesSerializer(movie)
            return Response(serializer.data)
        except Movies.DoesNotExist:
            serializer = MoviesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return self.create(request, *args, **kwargs)


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        if 'movie_id' in self.kwargs:
            return Comments.objects.filter(movie_id=self.kwargs['movie_id'])
        else:
            return Comments.objects.all()


class TopListView(generics.ListAPIView):
    serializer_class = TopMoviesSerializer

    def get(self, request, *args, **kwargs):
        # optional date range filtering here:
        if 'from' in kwargs and 'to' in kwargs:
            datetime_from = timezone.make_aware(datetime.strptime(kwargs['from'], '%Y-%m-%d'), timezone.get_current_timezone())
            datetime_to = timezone.make_aware(datetime.strptime(kwargs['to'], '%Y-%m-%d'), timezone.get_current_timezone())
            count_query = Count('comments', filter=Q(
                comments__created__gte=datetime_from, comments__created__lte=datetime_to
            ))
        else:
            count_query = Count('comments')
        queryset = Movies.objects \
            .annotate(comments_count=count_query) \
            .order_by('-comments_count')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
