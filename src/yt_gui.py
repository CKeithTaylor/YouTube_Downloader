from tkinter import *
from threading import Thread
from tkinter import filedialog, messagebox
from pytube import YouTube, Playlist


def download_complete(stream=None, file_path=None):
    print("Download complete")
    messagebox.showinfo("Message", "File has been downloaded...")
    dwnld_btn["text"] = "Download Video"
    dwnld_btn["state"] = "active"
    url_field.delete(0, END)


def progress_bar(stream=None, chunk=None, bytes_remaining=None):
    percent = round(100 * ((file_size - bytes_remaining) / file_size))
    dwnld_btn["text"] = f"""{percent}% of "{video_name}" downloaded"""


def download_file(url, save_directory):
    global file_size, video_name

    try:
        yt = YouTube(url)
        st = yt.streams.get_highest_resolution()
        file_size = st.filesize
        video_name = yt.title

        yt.register_on_complete_callback(download_complete)
        yt.register_on_progress_callback(progress_bar)

        st.download(output_path=save_directory)

    except Exception as e:
        print(e)
        print("Something went wrong")


def download_start(url):
    save_directory = filedialog.askdirectory()
    if save_directory is None:
        return

    try:
        check = url.split("/")[3]
        if check[0:8] == "playlist":
            p = Playlist(url)
            for video in p.video_urls:
                download_file(video, save_directory)
        else:
            download_file(url, save_directory)

    except Exception as e:
        print(e)
        print("please check the url")


def start_button():
    try:
        dwnld_btn["text"] = "Please wait while file(s) are downloaded"
        dwnld_btn["state"] = "disabled"
        url = url_field.get()
        if url == "":
            return
        print(url)
        thread = Thread(target=download_start, args=(url,))
        thread.start()
    except Exception as e:
        print(e)


root = Tk()
root.title("YouTube Downloader")
# root.iconbitmap("YouTube_23392.ico")
root.geometry("640x400")
img = PhotoImage(file="YouTube_23392.ico")
root.tk.call("wm", "iconphoto", root._w, img)

img_file = PhotoImage(file="YouTube_23392_img.png")
head_icon = Label(root, image=img_file)
head_icon.pack(side=TOP, pady=5)

url_field = Entry(root, font=("courier", 10), justify=CENTER)
url_field.pack(side=TOP, fill=X, padx=25, pady=15)
url_field.focus()

dwnld_btn = Button(
    root,
    text="Download Video or Playlist",
    font=("courier", 16),
    relief="ridge",
    command=start_button,
)
dwnld_btn.pack(side=TOP, pady=20)


root.mainloop()
