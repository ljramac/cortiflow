from sys import argv
from flask import Flask
from .v1.server import mount as v1
from .middlewares.config import mount as config
from .middlewares.database import mount as database


def create_app():
    app = Flask(__name__)

    return {
        "app": app,
        "run": app.run,
        "mount": lambda *funcs: [func(app) for func in funcs]
    }


if __name__ == '__main__':
    created_app = create_app()
    created_app["mount"](config, database, v1)
    created_app["run"](debug="--debug" in argv)
