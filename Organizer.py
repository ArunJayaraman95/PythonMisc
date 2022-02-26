import os
import shutil
import pywintypes
from win10toast import ToastNotifier

image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm"]
docs_formats = ["txt"]
trash_formats = ["exe"]
toast = ToastNotifier()
toast.show_toast("File Organizer", "Sorting has begun", duration = 15)

os.chdir(r"C:\Users\ripar\Downloads")
i = 1
while i < 5:
    files = os.listdir("./")
    i += 1
    for file in files:
        if os.path.isfile(file) and file != "Organizer.py":
            ext = (file.split(".")[-1]).lower()

            if ext in image_formats:
                shutil.move(file, r"C:/Users/ripar/Pictures/" + file)
            if ext in audio_formats:
                shutil.move(file, r"C:/Users/ripar/Blender/Audio/" + file)
            if ext in video_formats:
                shutil.move(file, r"C:/Users/ripar/Pictures/" + file)
            if ext in docs_formats:
                shutil.move(file, r"C:/Users/ripar/Documents/Help/" + file)
            if ext in docs_formats:
                shutil.move(file, r"C:/Users/ripar/Documents/Trash/" + file)
            else:
                shutil.move(file, r"C:/Users/ripar/Documents/To be Sorted/" + file)