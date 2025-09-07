from rest_framework.views import APIView
from rest_framework.response import Response
from .services import fetch_videos_with_metadata

class VideoListView(APIView):
    """
    GET /api/videos/
    Returns enriched video metadata from YouTube
    """
    def get(self, request):
        videos = fetch_videos_with_metadata()
        return Response(videos)
