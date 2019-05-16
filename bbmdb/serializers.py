#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from rest_framework import serializers
from .models import Movies, Comments


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("title", "year", "imdb_rating", "director")


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("movie_id", "content")

