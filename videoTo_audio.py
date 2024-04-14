from pytube import YouTube
from moviepy.editor import *

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=orftuB_yvMg"

# Output audio file path
audio_path = 'output_audio.mp3'

# Download the YouTube video
yt = YouTube(video_url)
yt.streams.filter(file_extension='mp4').first().download(output_path='.', filename='temp_video')

# Rename the downloaded video file
import os
os.rename('temp_video.mp4', "output.mp4")
"""
# Load the downloaded video
video = VideoFileClip('temp_video.mp4')

# Extract audio from the video
audio = video.audio

# Write the audio to a file
audio.write_audiofile(audio_path)

# Close the video and audio objects
video.close()
audio.close()

# Delete the temporary video file
os.remove('temp_video.mp4')"""

print("Audio extracted successfully!")
