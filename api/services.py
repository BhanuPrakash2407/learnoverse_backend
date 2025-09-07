import requests
from django.conf import settings
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client['learnoverse']
video_collection = db['videos']  # MongoDB collection

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/videos"

def fetch_videos_with_metadata():
    """
    Fetch video IDs from MongoDB and enrich with YouTube metadata
    """
    # 1️⃣ Fetch video IDs
    video_docs = video_collection.find({}, {"videoId": 1, "_id": 0})
    video_ids = [v['videoId'] for v in video_docs]
    print(video_ids)

    if not video_ids:
        return []

    # 2️⃣ Fetch metadata from YouTube API
    params = {
        "part": "snippet,contentDetails",
        "id": ",".join(video_ids),
        "key": settings.YT_API_KEY
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    data = response.json()

    # 3️⃣ Transform response
    enriched_videos = []
    for item in data.get("items", []):
        enriched_videos.append({
            "videoId": item["id"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
            "duration": item["contentDetails"]["duration"]
        })

    return enriched_videos
