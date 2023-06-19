from pytube import Playlist
import pytube
import os
from music import download_song

def download_playlist():
    address = input("Enter playlist URL:\n")
    p = Playlist(url=address)

    # Press enter to create new folder in working directory
    print("Enter destination path")
    destination = str(input(" ")) or "."
    
    if destination == ".":
        destination = f".\{p.title}"

    try:
        print(f'Downloading: {p.title}')
    except KeyError:
        print("Downloading song...")
        download_song(address, destination)
        return None

    for video in p.videos:
        try:
            #selecting the stream
            vid = video.streams.filter(only_audio=True).first() 
        except pytube.exceptions.AgeRestrictedError:
            print("This song is age restricted")
            continue
            

        out_file = vid.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print(video.title + " has been downloaded")

download_playlist()