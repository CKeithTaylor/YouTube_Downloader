import os
from pytube import YouTube
from pytube import Playlist


def pl_dwnld(url):
    p = Playlist(url)
    print(f"Downloading: {p.title}")
    for video in p.video_urls:
        yt = YouTube(video)
        print(yt.title)
        yt.streams.get_highest_resolution().download()


def vid_dwnld(url):
    yt = YouTube(url)
    print(f"Downloading: {yt.title}")
    yt.streams.get_highest_resolution().download()


def set_dir():
    try:
        os.mkdir("C:/youtube_downloads")
        os.chdir("C:/youtube_downloads")
    except FileExistsError:
        os.chdir("C:/youtube_downloads")


def main(url):
    set_dir()
    check = url.split("/")[3]
    if check[0:8] == "playlist":
        pl_dwnld(url)
    else:
        vid_dwnld(url)


if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLBf0hzazHTGOEuhPQSnq-Ej8jRyXxfYvl"
    main(url)

print("********All Done!********")
