from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Song
from .serializer import SongSerializer


class SongApi(APIView):
    @staticmethod
    def getSong():
        songs = Song.objects.all()
        serialized_songs = SongSerializer(songs, many=True)
        return serialized_songs.data

    @staticmethod
    def addSong(data):
        song = Song.objects.filter(title=data["title"])
        if song:
            return {"error": "Song with same title exists"}
        serialized_song = SongSerializer(data=data)
        if serialized_song.is_valid():
            serialized_song.save()
            return serialized_song.data
        return serialized_song.errors

    @staticmethod
    def removeSong(data):
        try:
            # print(data)
            song = Song.objects.get(title=data["title"])
            song.delete()
            response = {"success": "deleted song"}
            return response
        except:
            return {"error": "No song Found"}

    @staticmethod
    def updateSong(data):
        try:
            song = Song.objects.get(id=data["id"])
            serialized_song = SongSerializer(song, data=data, partial=True)
            if serialized_song.is_valid():
                serialized_song.save()
                return serialized_song.data
            return serialized_song.errors
        except:
            return {"error": "No song Found"}

    def get(self, request):
        return Response(SongApi.getSong())

    def post(self, request):
        return Response(SongApi.addSong(request.data))

    def patch(self, request):
        return Response(SongApi.updateSong(request.data))

    def delete(self, request):
        return Response(SongApi.removeSong(request.data))
