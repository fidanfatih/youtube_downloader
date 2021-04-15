from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
#Creating youtube object with URL
file_size = 0

def progress(stream, chunk, file_handle, remaining=None):
    file_downloaded = (file_size - file_handle)
    per = float((file_downloaded/file_size)*100)
    Dbtn.config(text = "{:00.0f} %Downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlFIeld.get()
        print(url)
        Dbtn.config(text='Downloading', state=DISABLED)
        path_to_save = askdirectory()
        print(path_to_save)
        vid = YouTube(url, on_progress_callback=progress)
        strm = vid.streams.first()
        file_size = strm.filesize
        print(file_size)
        VTitle.config(text=strm.title)
        VTitle.pack(side = TOP)
        print("We Found the streams")
        if path_to_save is None:
            return
        else:
            strm.download(path_to_save)
            urlFIeld.delete(0,END)
            showinfo("Download Finished", "Downloaded Successfully")
            VTitle.config(text="")
            Dbtn.config(text="Start Download", state=NORMAL)
    except Exception as e:
        print(e)
        print("Error!!")

def startDownloadT():
    thrd=Thread(target=startDownload)
    thrd.start()

#Started GUI Building
main = Tk()
C = Canvas(main,height=50, width=300)

C.pack()
main.title("Youtube Video Downloader")

main.geometry("600x200")
urlFIeld = Entry(main,font=("verdana", 15),justify=CENTER)
urlFIeld.pack(side=TOP,fill=X,padx=10)

Dbtn=Button(main, text="Start Download", font= ("verdana",18), relief="ridge",command = startDownloadT)
Dbtn.pack(side=TOP)

VTitle = Label(main, text = "Video Title")
main.mainloop()