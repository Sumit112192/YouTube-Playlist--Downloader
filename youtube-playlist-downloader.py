from pytube.contrib.playlist import Playlist
from pytube import YouTube
from pytube.cli import on_progress

url = input("Enter Playlist URL: ")
playlist = Playlist(url)
print("Total Videos: ",len(playlist.video_urls))

for video_url in playlist.video_urls:
    yt=YouTube(video_url,on_progress_callback=on_progress)
    stream=yt.streams.get_highest_resolution()
    print(yt.title)
    stream.download(filename=yt.title+".mp4")




    
    










