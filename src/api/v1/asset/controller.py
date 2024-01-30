from .model import Asset
from ..storage.filesystem import FileSystem


def find(_):
    return Asset().find(), 200


def upload(request):
    files = request.files.getlist("files")

    for file in files:
        fs = FileSystem()

        asset = Asset(fs.save(file))

        asset.create()

    return "Created", 201
