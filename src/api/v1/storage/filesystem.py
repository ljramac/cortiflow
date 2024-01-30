from flask import current_app
from os import path


class FileSystem:
    def __init__(self):
        pass

    def save(self, file):
        upload_dir = current_app.config.get("UPLOAD_FOLDER")

        filepath = path.abspath(path.join(upload_dir, file.filename))

        file.save(dst=filepath)

        return filepath
