from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employees = db.relationship('employee', backref='department')

    def __init__(self, *args, **kwargs):
        super(Department, self).__init__(self, *args, **kwargs)
