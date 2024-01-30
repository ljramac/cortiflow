from os import path, environ


def mount(app):
    for key, value in [[key, environ[key]] for key in [key for key in environ.keys() if "FLASK_CONFIG_" in key]]:
        app.config[key.replace("FLASK_CONFIG_", "")] = value

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path.abspath('')}/db/sqlite/{app.config.get('FLASK_ENV')}.db"
