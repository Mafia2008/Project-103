import sys
import time
import random
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from_dir = "C:/Users/zarif/Downloads/Coding/103/project"

class FileCreatedChecker(FileSystemEventHandler):
    def on_created(self, event):
        print("Someone created ",{event.src_path})
    def on_deleted(self, event):
        print("Someone deleted ",{event.src_path})

eventHandler = FileCreatedChecker()
observer = Observer()
observer.schedule(eventHandler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
