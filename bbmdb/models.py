#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.db import models
import omdb

API_KEY='95667d5d'
omdb.set_default('apikey', API_KEY)


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=True)
    imdb_rating = models.FloatField(max_length=1, null=True)
    director = models.CharField(max_length=255, null=True)

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


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movies, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {} ({})".format(self.comment_id, self.content, self.created)

