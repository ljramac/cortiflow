import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.start_process()  # Iniciar el proceso al crear el manejador

    def on_any_event(self, event):
        print(f'Changes detected. Restarting {self.command}')
        self.start_process()

    def start_process(self):
        if hasattr(self, 'process'):  # Si el proceso existe, terminarlo antes de iniciar uno nuevo
            self.process.terminate()
        self.process = subprocess.Popen(self.command, shell=True)


if __name__ == "__main__":
    event_handler = MyHandler(
        "pipenv run python -u -m src.api --debug")
    observer = Observer()
    observer.schedule(event_handler, "./src/api", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.terminate()  # Asegurarse de terminar el proceso al salir

    observer.join()
