from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ModelUtils(db.Model):
    __abstract__ = True

    def set(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Base(ModelUtils):
    __abstract__ = True
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String(32), nullable=False)
    updated_by = db.Column(db.String(32), nullable=False)
    meta = db.Column(db.JSON)

    def classify(self):
        pass

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id=id)

    @classmethod
    def find(cls, **kwargs):
        result = cls.query.filter_by(**kwargs).all()

        return [item.to_dict() for item in result]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def create(self, **kwargs):
        self.classify()

        self.set(kwargs)

        return self.save()

    def update(self, **kwargs):
        self.set(kwargs)

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
