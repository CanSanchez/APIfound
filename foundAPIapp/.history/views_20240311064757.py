from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Post.objects.all(),
    serializer_class = PostSerializer


class PostList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Post.objects.all()
    serializer_class = PostSerializer
