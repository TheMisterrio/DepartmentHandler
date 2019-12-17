"""Employee model for SQLAlchemy"""
from rest.api import db


class Employee(db.Model):
    """Employee model for SQLAlchemy"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id', onupdate='CASCADE', ondelete='CASCADE'))
    date_of_birthday = db.Column(db.Date)
    salary = db.Column(db.DECIMAL)

    def __eq__(self, other):
        """
        Compares employees
        :param Department other: compare with this employee
        :return: result of comparing
        :rtype: bool
        """
        if (self.id == other.id) and (self.name == self.name) and (self.department_id == other.department_id) and \
                (self.date_of_birthday == other.date_of_birthday) and (self.salary == other.salary):
            return True
        return False

    def __hash__(self):
        return self.id

    def __repr__(self):
        return f'<Employee> name = {self.name}'
