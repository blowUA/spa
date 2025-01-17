from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Sample, Page, Item

class SampleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Sample
        fields = ('id', 'created', 'name', 'img_name', 'image', 'url', 'owner', 'info')

class PageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Page
        fields = ('id', 'created', 'pageid', 'header', 'message', 'url', 'urltext', 'owner', 'project')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Item
        fields = ('id', 'created', 'page', 'name', 'url', 'image', 'urltext', 'owner', 'info', 'button')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    sample = serializers.HyperlinkedRelatedField(many=True, view_name='sample-detail', read_only=True)
    page = serializers.HyperlinkedRelatedField(many=True, view_name='page-detail', read_only=True)
    items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'sample', 'page', 'items')
