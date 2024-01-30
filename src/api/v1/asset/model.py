from flask import current_app
from datetime import datetime
from os import path
from ...database import db, Base
from ...helpers import get_md5


class Asset(Base):
    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filepath = db.Column(db.String(255), unique=True, nullable=False)
    size = db.Column(db.BigInteger, nullable=False)
    md5 = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    error_message = db.Column(db.String(255))
    related_files = db.Column(db.PickleType)

    def __init__(self, filepath=None):
        self.filepath = filepath

    def classify(self):
        timestamp = datetime.now()
        hostname = current_app.config.get("HOSTNAME")

        self.size = path.getsize(self.filepath)
        self.md5 = get_md5(self.filepath)
        self.status = "uploaded"
        self.error_message = None
        self.related_files = tuple()
        self.created_at = timestamp
        self.updated_at = timestamp
        self.created_by = hostname
        self.updated_by = hostname

        return
