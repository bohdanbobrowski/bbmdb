#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movies, Comments
from .serializers import MoviesSerializer, MoviesListSerializer, CommentsSerializer


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
        serialized = MoviesListSerializer(expected, many=True)
        self.assertEqual(response.data['results'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_movie(self):
        response = self.client.post('/movies', {'title': "The Grapes of Wrath"})
        self.assertEqual(response.data['movie_id'], 1)
        self.assertEqual(response.data['year'], 1940)
        self.assertEqual(response.data['director'], 'John Ford')
        self.assertEqual(response.data['comments_count'], 2)

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

    def test_get_comments_for_selected_movie_id(self):
        response = self.client.get('/comments/1')
        expected = Comments.objects.filter(movie_id=1)
        serialized = CommentsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comment(self):
        response = self.client.post('/comments', {'movie_id': 1, "content": "What a great movie!"})
        self.assertEqual(response.data['movie_id'], 1)
        self.assertEqual(response.data['comment_id'], 4)


class TopTest(BaseViewTest):

    def test_top_list(self):
        response = self.client.get('/top')
        self.assertEqual(response.data[0]['comments_count'], 2)
        self.assertEqual(response.data[1]['comments_count'], 1)

    def test_top_list_filteres(self):
        response = self.client.get('/top/1939-09-01/1945-05-08')
        self.assertEqual(response.data[0]['comments_count'], 0)
        self.assertEqual(response.data[1]['comments_count'], 0)
