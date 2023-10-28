import os
import base64
import urllib3
import json
import time
from dotenv import load_dotenv
from pypexels import PyPexels
import requests
#set working directory
os.getcwd()
class Adobe:
# loading credentials
    def __init__(self):
        load_dotenv(".env")
        self.username = os.getenv('ADOBE_USERNAME')
        self.password = os.getenv('ADOBE_PASSWORD')
        self.pexels_key=os.getenv('PEXELS_KEY')
# downloading free royakty clips from Adobe Stock
    def search_clips(self,topic:str,number_of_clips:int):
    # Search parameters
        api_url="https://api.pexels.com/videos/"
        query = topic  # Your desired topic
        per_page = number_of_clips  # Number of videos per page
        self.number_of_clips=number_of_clips
        # Make the API request
        api_key=self.pexels_key 
        # Create API object
        py_pexel = PyPexels(api_key=api_key)
        search_videos_page = py_pexel.videos_search(query=topic, per_page=40)
        # Search for videos
        # Print video details
        return search_videos_page
    def download_clips(self,videos):   
        iterator=0
        number_of_clips=self.number_of_clips
        for video in videos:
            if iterator < number_of_clips:
                print(video.id, video.user.get('name'), video.url)
                data_url = 'https://www.pexels.com/video/' + str(video.id) + '/download'
                get_videos = requests.get(data_url)
                print(get_videos.headers.get('content-type'))
                iterator=iterator+1
# getting videos one by one
                if get_videos.headers.get('content-type') == 'video/mp4':
                    with open('video' + str(iterator) + '.mp4', 'wb') as f:
                        f.write(get_videos.content)
            else:
                break  
                   


