#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.db import models


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    year = models.IntegerField()
    imdb_rating = models.FloatField(max_length=1)
    director = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}. {} [{}] {} - {}/10".format(self.movie_id, self.title, self.year, self.imdb_rating, self.director)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {} ({})".format(self.comment_id, self.content, self.created)
