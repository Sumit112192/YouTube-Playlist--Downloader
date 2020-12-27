from pytube import Playlist
from pytube import YouTube
global check
check = True
global file_size
def progress(stream,chunk,file_handle,bytes_remaining=None):
    check=False
    file_downloaded = file_size-file_handle
    per=(file_downloaded/file_size)*100
    if int(per)==100:
        print("Downloaded")
    
url = input("Enter Playlist URL:")
playlist = Playlist(url)
print("Videos=",len(playlist.video_urls))
verify = input("Should I download for u?")
global i
i=1
if verify.lower() =="yes" and check==True:
    for video_url in playlist.video_urls:
        yt=YouTube(video_url,on_progress_callback=progress)
        stream=yt.streams.get_highest_resolution()
        file_size=stream.filesize
        print(i,yt.title,"\n")
        
        stream.download(filename=str(i)+".mp4")
        i+=1
elif verify.lower()=="no":
    print("As your wish \n Have a nice day")
else:
    print("Either yes or no")



    
    










