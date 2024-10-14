import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        print(f"Starting process: {self.command}")
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print(f"Detected change in {event.src_path}. Restarting...")
            if self.process:
                self.process.terminate()
                self.process.wait()
            self.start_process()


if __name__ == "__main__":
    path = "./gui"  # Monitor the gui directory
    command = f"{sys.executable} main.py"  # Command to restart the application
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Monitoring {path} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping observer and subprocess...")
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
            event_handler.process.wait()
    observer.join()
