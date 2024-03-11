from rest_framework import serializers
from .models import Customer

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['pk', 'petname', 'lastlocation', 'createdat']