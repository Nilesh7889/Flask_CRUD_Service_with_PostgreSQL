from app import db


# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    services = db.Column(db.JSON)

    def __repr__(self):
        return f'<User {self.id}: {self.full_name}>'
