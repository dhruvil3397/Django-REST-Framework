from django.db.models import fields
from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # Mention the singer's song in this serializer
    song = serializers.StringRelatedField(many=True,read_only = True)  # Give name of the song
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only = True) # Give id of the song

    # Give the Hyperlink of the song :-- "http://127.0.0.1:8000/song/1/"    
    # song = serializers.HyperlinkedRelatedField(many=True,read_only = True,view_name='song-detail')

    # It returns the slug_field value
    # song = serializers.SlugRelatedField(many=True,read_only = True,slug_field='title')

    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id','name','gender','song']