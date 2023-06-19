from pytube import YouTube
import os

def download_song(address, destination):

    yt = YouTube(address)

    video = yt.streams.filter(only_audio=True).first() #selecting the stream

    out_file = video.download(output_path=destination)
    print(out_file)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print(yt.title + " has been downloaded")

