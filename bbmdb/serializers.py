#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from rest_framework import serializers
from .models import Movie, Comment


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "year", "imdb_rating", "director")


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("movie_id", "content")

