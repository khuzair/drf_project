from pyexpat import model
from rest_framework import serializers
from .models import Song, Singer



# model serializer
class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'release_year', 'singer']


# nested serializer
class SingerModelNestedSerializer(serializers.ModelSerializer):
    song = SongModelSerializer(many=True) # it will grab all fields data from that models
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # song = serializers.HyperlinkedIdentityField(view_name='drfrelationsapi:song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'style', 'song']


# hyperlinked model serializer
class SingerHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title') # you have to model field name in a slup_field
    url = serializers.HyperlinkedIdentityField(view_name="drfrelationsapi:singer-detail")
    class Meta:
        model = Singer
        fields = ['id', 'name', 'url', 'style', 'song']