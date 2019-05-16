#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from rest_framework import serializers
from .models import Movies, Comments


class MoviesSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ("movie_id", "title", "year", "imdb_rating", "director", "comments_count")

    def get_comments_count(self, obj):
        return obj.comments.count()


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("comment_id", "movie_id", "content", "created")


class TopMoviesSerializer(MoviesSerializer):
    rank = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ("movie_id", "rank", "comments_count")

    def get_rank(self, obj):
        return 0
