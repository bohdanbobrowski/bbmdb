#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.urls import path
from bbmdb.views import MoviesListView, CommentsListView, MovieCommentsView, TopListView

urlpatterns = [
    path('movies', MoviesListView.as_view()),
    path('comments', CommentsListView.as_view()),
    path('comments/<movie_id>', MovieCommentsView.as_view()),
    path('top', TopListView.as_view()),
]
