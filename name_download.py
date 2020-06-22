import os
from apiclient.discovery import build


def youtube_search_keyword(query, max_results):
    # calling the search.list method to
    # retrieve youtube search results
    search_keyword = youtube_object.search().list(q=query, part="snippet",
                                                  maxResults=max_results).execute()
    # extracting the results from search response
    results = search_keyword.get("items", [])
    vid_id = results[0]["id"]['videoId']
    return vid_id


# Arguments that need to passed to the build function
DEVELOPER_KEY = "YOUR_API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)
fl = open("song.txt", "r")
z = fl.readlines()
a = z[0]
a = a.split(",")
fl.close()
os.chdir("/home/adarsha/Music")
os.system("pwd")
n = len(a)
i = 0
while i < n:
    vid_name = a[i]
    vid_id = youtube_search_keyword(vid_name, max_results=1)
    song_link = "youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v="+vid_id
    os.system(song_link)
    i = i+1
