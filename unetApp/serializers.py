from rest_framework import serializers
from .models import Images

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['unMaskedImage']