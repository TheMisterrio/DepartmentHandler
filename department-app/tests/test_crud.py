import unittest
from datetime import date
from decimal import Decimal
from models.department import Department
from models.employee import Employee
from service import crud
from .base import BaseTestCase


class TestDepartments(BaseTestCase):
    """Tests for Departments class from service.crud"""
    def test_get_all(self):
        self.assertEqual(crud.Departments.get_all(), [Department(id=10001, employees=[
            Employee(id=1, name='Steven Gray', department_id=10001, date_of_birthday=date(1997, 10, 1),
                     salary=Decimal(1000)),
            Employee(id=2, name='John Spins', department_id=10001, date_of_birthday=date(1997, 5, 11),
                     salary=Decimal(3000))])])

    def test_get(self):
        self.assertEqual(crud.Departments.get(10001), Department(id=10001, employees=[
            Employee(id=1, name='Steven Gray', department_id=10001, date_of_birthday=date(1997, 10, 1),
                     salary=Decimal(1000)),
            Employee(id=2, name='John Spins', department_id=10001, date_of_birthday=date(1997, 5, 11),
                     salary=Decimal(3000))]))

    def test_add(self):
        self.assertEqual(crud.Departments.add(10002), Department(id=10002, employees=[]))

    def test_update(self):
        self.assertEqual(crud.Departments.update(10001, 10002), Department(id=10002, employees=[
            Employee(id=1, name='Steven Gray', department_id=10002, date_of_birthday=date(1997, 10, 1),
                     salary=Decimal(1000)),
            Employee(id=2, name='John Spins', department_id=10002, date_of_birthday=date(1997, 5, 11),
                     salary=Decimal(3000))]))

    def test_delete(self):
        crud.Departments.delete(10001)
        self.assertRaises(AttributeError, crud.Departments.get, 10001)


class TestEmployees(BaseTestCase):
    """Tests for Employees class from service.crud"""
    def test_get_all(self):
        self.assertEqual(crud.Employees.get_all(), [
            Employee(id=1, name='Steven Gray', department_id=10001, date_of_birthday=date(1997, 10, 1),
                     salary=Decimal(1000)),
            Employee(id=2, name='John Spins', department_id=10001, date_of_birthday=date(1997, 5, 11),
                     salary=Decimal(3000))
            ])

    def test_get(self):
        self.assertEqual(crud.Employees.get(1), Employee(id=1, name='Steven Gray', department_id=10001,
                                                         date_of_birthday=date(1997, 10, 1), salary=Decimal(1000)))

    def test_add(self):
        self.assertEqual(crud.Employees.add('Chris Smith', 10001, date(1999, 1, 1), Decimal(5000)),
                         Employee(id=3, name='Chris Smith', department_id=10001, date_of_birthday=date(1999, 1, 1),
                                  salary=Decimal(5000)))

    def test_update(self):
        self.assertEqual(crud.Employees.update(2, 'John Color', 10001, date(1999, 10, 1), Decimal(6000)),
                         Employee(id=2, name='John Color', department_id=10001, date_of_birthday=date(1999, 10, 1),
                                  salary=Decimal(6000)))

    def test_delete(self):
        crud.Employees.delete(1)
        self.assertRaises(AttributeError, crud.Employees.get, 1)

