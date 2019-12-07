from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    date_of_birthday = db.Column(db.Date)
    salary = db.Column(db.DECIMAL)

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
