from pytube import YouTube

# URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=iyUR6PANjJk'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download(output_path='path/to/your/download/directory')

print(f'Video downloaded successfully: {video_stream.title}')
