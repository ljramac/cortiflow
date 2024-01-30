from flask import Flask, Blueprint
from .asset.router import assets_blueprint


def mount(app):
    api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

    @api_blueprint.route("/health")
    def index():
        return "Alive!", 200

    app.register_blueprint(api_blueprint)
    app.register_blueprint(assets_blueprint)

    return app


if __name__ == '__main__':
    mount()
