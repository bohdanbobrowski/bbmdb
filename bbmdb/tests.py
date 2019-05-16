#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movie, Comment
from .serializers import MoviesSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_movie(title, year, imdb_rating, director):
        Movie.objects.create(title=title, year=year, imdb_rating=imdb_rating, director=director)

    @staticmethod
    def add_comment(movie_id, comment):
        Comment.objects.create(movie_id=movie_id,comment=comment)

    def setUp(self):
        self.add_movie("The Grapes of Wrath", 1940, 8.1, "John Ford")
        self.add_movie("Detective Story", 1952, 7.6, "William Wyler")
        self.add_movie("Baza ludzi umarlych", 1959, 7.5, "Czeslaw Petelski")
        self.add_movie("Knife in the Water", 1962, 7.6, "Roman Polanski")
        self.add_movie("The Saragossa Manuscript", 1965, 8, "Wojciech Has")
        self.add_comment(1,"Brilliant!")
        self.add_comment(1, "Fantastic!")
        self.add_comment(2, "Wonderfull!")


class MoviesTest(BaseViewTest):

    def test_get_all_movies(self):
        response = self.client.get(
            reverse('movies')
        )
        expected = Movie.objects.all()
        serialized = MoviesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_movie(self):
        response = self.client.post(
            reverse('movies'),
            {'title': "Baza ludzi umarlych"},
            format="json"
        )

    def test_get_new_movie(self):
        response = self.client.post(
            reverse('movies'),
            {'title': "Detective Story"},
            format="json"
        )


class CommentsTest(BaseViewTest):

    def test_get_comments(self):
        response = self.client.get(
            reverse('comments')
        )

    def test_post_comment(self):
        response = self.client.post(
            reverse('comments'),
            {'movie_id': 1, "comment": "What a great movie!"},
            format="json"
        )
