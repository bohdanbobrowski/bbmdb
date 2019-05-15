#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Bohdan Bobrowski bohdan@bobrowski.com.pl

from django.urls import path
from bbmdb.views import MoviesView, CommentsView

urlpatterns = [
    path('movies', MoviesView.as_view()),
    path('comments', CommentsView.as_view()),
]
