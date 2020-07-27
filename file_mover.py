import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(folder_to_track):
            # split na ime i ekstenziju
            filename, extension = os.path.splitext(filename)
            # biraj ekstenziju
            if extension == '.py':
                src = folder_to_track + "/" + filename + extension
                new_destination = folder_destination + "/" + filename + extension
                os.rename(src, new_destination)


folder_to_track = "/Users/Nikola/Downloads"
folder_destination = "/Users/Nikola/Desktop"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
