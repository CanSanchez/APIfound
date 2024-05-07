from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'pk', 
            'petname', 
            'petimage',
            'pettype',
            'petcolor',
            'petbreed',
            'petdescription', 
            'lastlocation', 
            'contactphone',
            'contactemail', 
            'createdat']