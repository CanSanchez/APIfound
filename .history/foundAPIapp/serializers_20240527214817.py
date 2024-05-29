from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id', 
            'petname', 
            'petimage',
            'pettype',
            'petcolor',
            'petbreed',
            'petdescription', 
            'lastlocation', 
            'contactphone',
            'contactemail',
            'formtype', 
            'createdat',
            'updatedat'
        ]