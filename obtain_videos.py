import pytube 
from pytube import YouTube
from pytube import Search
import os
os.getcwd()
class Youtube:
    def youtube_search(topic: str, number_of_clips: int)-> list:        
        youtube_videos=Search(topic)
        list_of_videos=[]
        for video in youtube_videos.results:
            list_of_videos.append(f"{video.title}\n{video.watch_url}\n")
        return list_of_videos
    def download_video(url: str)-> str:
        yt = YouTube(url)
        yt.streams.first().download()
        message_of_success=f"Video {yt.title} has been downloaded"
        return message_of_success    
