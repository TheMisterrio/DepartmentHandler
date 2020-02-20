"""Settings for tests"""
import unittest
from datetime import date
from decimal import Decimal
from rest.api import app, db
from models.department import Department
from models.employee import Employee
from config import TestConfiguration


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfiguration)
        self.app = app.test_client()
        db.create_all()
        db.session.add(Department(id=10001, name='Test Department'))
        db.session.add(
            Employee(name='Steven Gray', department_id=10001, date_of_birthday=date(1997, 10, 1),
                     salary=Decimal(1000)))
        db.session.add(
            Employee(name='John Spins', department_id=10001, date_of_birthday=date(1997, 5, 11),
                     salary=Decimal(3000)))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
