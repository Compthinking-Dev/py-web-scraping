import googleapiclient.discovery
import json


API_KEY = "YOUR_API_KEY"


def get_channel(channel_id):
    youtube = googleapiclient.discovery.build(
        serviceName="youtube", version="v3", developerKey=API_KEY)
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    resp = request.execute()
    info = {
        "title": resp["items"][0]["snippet"]["title"],
        "description": resp["items"][0]["snippet"]["description"],
        "viewCount": resp["items"][0]["statistics"]["viewCount"],
        "subscriberCount": resp["items"][0]["statistics"]["subscriberCount"],
        "videoCount": resp["items"][0]["statistics"]["videoCount"],
        "upload_playlist": resp["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    }
    return info


def get_video_ids(playlist_id):
    youtube = googleapiclient.discovery.build(
        serviceName="youtube", version="v3", developerKey=API_KEY)

    video_ids = []
    next_page_token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=playlist_id,
            pageToken=next_page_token
        )
        resp = request.execute()

        for item in resp["items"]:
            video_ids.append(item["snippet"]["resourceId"]["videoId"])
        print(f"Got {len(video_ids)} video ids")

        next_page_token = resp.get("nextPageToken", None)
        if not next_page_token:
            break

    return video_ids


def get_video_info(video_ids):
    youtube = googleapiclient.discovery.build(
        serviceName="youtube", version="v3", developerKey=API_KEY)
    videos = []
    for i, vid in enumerate(video_ids):
        print(f"Getting {vid} ({i+1}/{len(video_ids)})...")
        request = youtube.videos().list(
            part="snippet,statistics",
            id=vid
        )
        resp = request.execute()
        video = {
            "publishedAt": resp["items"][0]["snippet"]["publishedAt"],
            "title": resp["items"][0]["snippet"]["title"],
            "viewCount": resp["items"][0]["statistics"]["viewCount"],
            "commentCount": resp["items"][0]["statistics"]["commentCount"],
            "video_id": vid
        }
        videos.append(video)
    return videos


if __name__ == "__main__":
    print("Getting channel info")
    channel = get_channel("UCMUnInmOkrWN4gof9KlhNmQ")

    print("Getting video ids")
    video_ids = get_video_ids(channel["upload_playlist"])

    print("Getting video data")
    videos = get_video_info(video_ids)
    print(f"{len(videos)} retrieved. The first 3:")
    for v in videos[:3]:
        print(v)

    data = {
        "channel": channel,
        "videos": videos
    }
    with open("channel_videos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
