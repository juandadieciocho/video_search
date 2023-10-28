import os
from obtain_clips import Adobe
from obtain_videos import Youtube
import requests

class Main:
    def TopicSelection(self):
        topic=input("Enter the topic you want to search for: ")
        return topic
    def NumberOfClips(self):
        number_of_clips=int(input("Enter the number of clips you want to download: "))
        return number_of_clips
    def ApiSelection():
        api=input("Enter the API you want to use: ")
        return api
    def DownloadClips(self,api,topic,number_of_clips):
        if api=="Adobe":
            Adobe=Adobe()
            clips_urls=Adobe.search_clips(topic,number_of_clips)
            videos=clips_urls.entries
            Adobe.download_clips(videos)
        elif api=="Youtube":
            Youtube=Youtube()
            Youtube.search_videos(topic,number_of_clips)
        else:
            print("Please enter a valid API")
    

# Replace with your actual Adobe Stock API endpoint and access token

#https://www.pexels.com/search/videos/indian%20couple/

        
if __name__ == "__main__":
    Adobe=Adobe()
    Youtube=Youtube()
    main=Main()
    os.getcwd()
    topic=main.TopicSelection()
    number_of_clips=main.NumberOfClips()
    api=main.ApiSelection()
    main.DownloadClips(api,topic,number_of_clips)


    

    

#https://github.com/adobe/target-python-sdk/blob/main/samples/requirements.txt