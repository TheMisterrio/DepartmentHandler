"""Department model for SQLAlchemy"""
from rest.api import db


class Department(db.Model):
    """Department model for SQLAlchemy"""
    id = db.Column(db.Integer, primary_key=True)
    employees = db.relationship('Employee', backref='department')

    def __eq__(self, other):
        """
        Compares departments
        :param Department other: compare with this department
        :return: result of comparing
        :rtype: bool
        """
        if (self.id == other.id) and (self.employees == other.employees):
            return True
        return False

    def __hash__(self):
        return self.id

    def __repr__(self):
        return f'<Department id={self.id}>'
