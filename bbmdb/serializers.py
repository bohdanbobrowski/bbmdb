#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from rest_framework import serializers
from .models import Movies, Comments


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("movie_id", "title", "year", "imdb_rating", "director", "comments_count")


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("movie_id", "title")


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("comment_id", "movie_id", "content", "created")


class TopMoviesSerializer(MoviesSerializer):

    class Meta:
        model = Movies
        fields = ("movie_id", "ranking", "comments_count")
