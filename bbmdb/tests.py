#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentsSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_movie(title):
        return Movies.objects.create(title=title)

    @staticmethod
    def add_comment(movie, content):
        return Comments.objects.create(movie_id=movie, content=content)

    def setUp(self):
        movieA = self.add_movie("The Grapes of Wrath")
        movieB = self.add_movie("Knife in the Water")
        self.add_comment(movieA, "Brilliant!")
        self.add_comment(movieA, "Fantastic!")
        self.add_comment(movieB, "Wonderfull!")


class MoviesTest(BaseViewTest):

    def test_get_all_movies(self):
        response = self.client.get('/movies')
        expected = Movies.objects.all()
        serialized = MoviesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_movie(self):
        response = self.client.post('/movies', {'title': "The Grapes of Wrath"})
        self.assertEqual(response.data['movie_id'], 1)
        self.assertEqual(response.data['year'], 1940)
        self.assertEqual(response.data['director'], 'John Ford')

    def test_get_new_movie(self):
        for i in range(0, 2):
            response = self.client.post('/movies', {'title': "Detective story"})
            self.assertEqual(response.data['movie_id'], 3)


class CommentsTest(BaseViewTest):

    def test_get_comments(self):
        response = self.client.get('/comments')
        expected = Comments.objects.all()
        serialized = CommentsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comment(self):
        response = self.client.post('/comments', {'movie_id': 1, "comment": "What a great movie!"})
        print(response.data)
