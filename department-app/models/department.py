from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employees = db.relationship('Employee', backref='department')

    def __repr__(self):
        return f'<Department id={self.id}>'
