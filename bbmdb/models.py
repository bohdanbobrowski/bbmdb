#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl
import os

from django.db import models
import omdb
from django.db.models import Count
from rest_framework.pagination import LimitOffsetPagination

from api.settings import OMDB_API_KEY

omdb.set_default('apikey', OMDB_API_KEY)


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=True)
    imdb_rating = models.FloatField(max_length=1, null=True)
    director = models.CharField(max_length=255, null=True)

    def comments_count(self):
        return self.comments.count()

    def ranking(self):
        result = Movies.objects \
            .annotate(comments_count=Count('comments')) \
            .values('comments_count') \
            .distinct() \
            .filter(comments_count__gte=self.comments_count)\
            .order_by('-comments_count')
        return len(result)

    def save(self, *args, **kwargs):
        if not self.movie_id:
            omdb_data = omdb.title(self.title)
            if omdb_data:
                self.year = omdb_data['year']
                self.imdb_rating = omdb_data['imdb_rating']
                self.director = omdb_data['director']
        super(Movies, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {} [{}] {} - {}/10".format(self.movie_id, self.title, self.year, self.imdb_rating, self.director)


class MoviesPagination(LimitOffsetPagination):
    default_limit = 5


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movies, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {} ({})".format(self.comment_id, self.content, self.created)

