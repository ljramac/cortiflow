from ..database import db


def mount(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
