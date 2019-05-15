#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("title", "year", "imdb_rating", "director")
