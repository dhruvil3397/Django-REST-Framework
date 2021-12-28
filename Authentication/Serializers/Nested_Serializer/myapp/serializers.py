from django.db.models import fields
from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True,read_only =True)

    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

# Here It returns Nested List as below in frontend0:------------------------


[
    {
        "id": 1,
        "name": "Arijit Singh",
        "gender": "Male",
        "song": [
            {
                "id": 1,
                "title": "Tum hi ho",
                "singer": 1,
                "duration": 5
            },
            {
                "id": 2,
                "title": "Kabhi jo",
                "singer": 1,
                "duration": 8
            }
        ]
    },
    {
        "id": 2,
        "name": "Neha",
        "gender": "Female",
        "song": [
            {
                "id": 3,
                "title": "Pani",
                "singer": 2,
                "duration": 3
            }
        ]
    }
]