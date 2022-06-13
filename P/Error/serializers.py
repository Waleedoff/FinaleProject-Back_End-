from rest_framework import  serializers
from .models import ERROR
from .models import Comment

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ERROR
        fields = '__all__'




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'