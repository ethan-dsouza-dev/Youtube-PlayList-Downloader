from pytube import YouTube
import os



yt = YouTube(str(input("Enter URL of YouTube video:\n")))

video = yt.streams.filter(only_audio=True).first() #selecting the stream

print("Enter Destination address (leave blank to save in current dir)")
destination = str(input(" ")) or '.'

out_file = video.download(output_path=destination)
print(out_file)
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)
print(yt.title + " has been downloaded")

