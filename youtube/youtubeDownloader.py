from pytube import YouTube
from sys import argv

try:
    
    link = argv[1]
    yt = YouTube(link)
    print("Downloading with highest Resolution...")
    yd = yt.streams.get_highest_resolution()
    yd.download("/Users/luism/Desktop/youtubeDownloads")
    print("Successfully Downloaded: ", yt.title)

except Exception as e:
    print("Error Downloading: ", e)
