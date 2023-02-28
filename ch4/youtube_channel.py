import googleapiclient.discovery


API_KEY = "YOUR_API_KEY"


def channel(channel_id):
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


if __name__ == "__main__":
    channel = channel("UCMUnInmOkrWN4gof9KlhNmQ")
    for k, v in channel.items():
        print(f"{k}: {v}")
