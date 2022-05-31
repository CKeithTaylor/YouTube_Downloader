import os
from pytube import YouTube
from pytube import Playlist

### enter the full link to the video or playlist you want to download for the "url" variable ###

url = "##link here##"


def pl_dwnld(url):
    p = Playlist(url)
    set_dir(p.title)
    print(f"Downloading: {p.title}")
    for video in p.video_urls:
        yt = YouTube(video)
        print(yt.title)
        yt.streams.get_highest_resolution().download()


def vid_dwnld(url):
    yt = YouTube(url)
    set_dir(yt.title)
    print(f"Downloading: {yt.title}")
    yt.streams.get_highest_resolution().download()


def set_dir(dir):
    try:
        os.mkdir(f"C:/youtube_downloads/{dir}")
        os.chdir(f"C:/youtube_downloads/{dir}")
    except FileExistsError:
        os.chdir(f"C:/youtube_downloads/{dir}")


def main(url):
    check = url.split("/")[3]
    if check[0:8] == "playlist":
        pl_dwnld(url)
    else:
        vid_dwnld(url)


if __name__ == "__main__":
    main(url)

print("********All Done!********")
