from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
import shutil


#The askdirectory() comes with filedialog class in tkinter.
# The askdirectory() method includes a dialog box that only allows director
# and return directory path that the user selects.

def select_path ():
    url_path = filedialog.askdirectory()
    path_lable.config(text=url_path)

def download_file():
    #get user link
    get_link = linkfield.get()

    #get selected path
    user_path = path_lable.cget("text")
    screen.title ("DOWNLOADING....")

    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
     #shutil => move file to selected directory
    shutil.move (mp4_video , user_path)
    screen.title (" DOWNLOADING COMPLETE ")








screen = Tk() 
title = screen.title ( "youtube downloader ")
canvas = Canvas( screen , width=500 , height=500 )
canvas.pack()




#LINK POSITION
linkfield = Entry( screen , width=70 )
linklable = Label (screen , text= " PUT YOUR LINK HERE : " , font = 15)

#ADD WIDGETS 
canvas.create_window( 250 , 170 , window = linklable)
canvas.create_window( 250 , 220 , window = linkfield)

#SELECT PATH FOR SAVING 
path_lable = Label(screen, text= "select a path", font=15)
selc_butt = Button(screen, text=" SELECT PATH", command=select_path)

#ADD SELECT PATH AND SELECT PATH BUTTON TO THE WINDOW 
canvas.create_window(250,280,window=path_lable)
canvas.create_window(250, 315, window=selc_butt)

# MAKE DOWNLAOD BUTTON
download_bt = Button(screen, text="DOWNLOAD FILE", command=download_file)

#ADD DOWNLOAD BUTTON TO THE WINDOW
canvas.create_window( 250, 350, window=download_bt)



screen.mainloop()
