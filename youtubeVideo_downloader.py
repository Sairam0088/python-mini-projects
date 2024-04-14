#youtube video downloader using python

from pytube import YouTube

video_url = "https://youtu.be/EtPUD8cHNCE?si=gTp4PZOgfhrySTdt"
output_path = r"C:\Users\saira\Desktop\Python"

try:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    print("Vidoe downloaded successfully")

except Exception as e:
    print("Error:",e)