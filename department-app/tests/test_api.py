import unittest
from .base import BaseTestCase


class TestDepartments(BaseTestCase):
    """Tests for Department class from rest.api"""
    def test_get(self):
        request = self.app.get('/api/departments')
        self.assertEqual(request.json, {'ids': [10001], 'employees': [['Steven Gray', 'John Spins']]})
        self.assertEqual(request.status_code, 200)


class TestAddDepartment(BaseTestCase):
    def test_post_correct(self):
        request = self.app.post('api/department', data={'dep_id': 10002})
        self.assertEqual(request.json, {'id': '10002'})
        self.assertEqual(request.status_code, 201)

    def test_post_incorrect(self):
        request = self.app.post('api/department', data={'dep_id': 10001})
        self.assertEqual(request.status_code, 400)
        request = self.app.post('api/department', data={'dep_id': 'some string'})
        self.assertEqual(request.status_code, 400)


class TestDepartment(BaseTestCase):
    def test_get_correct(self):
        request = self.app.get('/api/department/10001')
        self.assertEqual(request.json, {'id': 10001, 'employees': ['Steven Gray', 'John Spins']})
        self.assertEqual(request.status_code, 200)

    def test_get_incorrect(self):
        request = self.app.get('/api/department/10005')
        self.assertEqual(request.status_code, 404)

    def test_put_correct(self):
        request = self.app.put('/api/department/10001', data={'dep_id': 10004})
        self.assertEqual(request.json, {'id': '10004'})
        self.assertEqual(request.status_code, 201)

    def test_put_incorrect(self):
        request = self.app.put('/api/department/10005', data={'dep_id': 10004})
        self.assertEqual(request.status_code, 404)

    def test_delete_correct(self):
        request = self.app.delete('/api/department/10001')
        self.assertEqual(request.json, {'id': '10001'})
        self.assertEqual(request.status_code, 200)

    def test_delete_incorrect(self):
        request = self.app.delete('/api/department/10005')
        self.assertEqual(request.status_code, 404)


class TestEmployees(BaseTestCase):
    def test_get(self):
        request = self.app.get('/api/employees')
        self.assertEqual(request.json, {'names': ['Steven Gray', 'John Spins'], 'departments': [10001, 10001],
                                        'dates_of_birthday': ['1997-10-01', '1997-05-11'],
                                        'salaries': ['1000', '3000']})
        self.assertEqual(request.status_code, 200)


class TestAddEmployee(BaseTestCase):
    def test_post_correct(self):
        request = self.app.post('/api/employee', data={'name': 'Sam Polo', 'department_id': 10001,
                                                       'date_of_birthday': '1998-01-01', 'salary': 2000})
        self.assertEqual(request.json, {'id': 3})
        self.assertEqual(request.status_code, 201)

    def test_post_incorrect(self):
        request = self.app.post('/api/employee', data={'name': 'Sam Polo', 'department_id': 10002,
                                                       'date_of_birthday': '1998-01-01', 'salary': 2000})
        self.assertEqual(request.status_code, 400)


class TestEmployee(BaseTestCase):
    def test_get_correct(self):
        request = self.app.get('/api/employee/1')
        self.assertEqual(request.json, {'name': 'Steven Gray', 'department_id': 10001,
                                        'date_of_birthday': '1997-10-01', 'salary': '1000'})
        self.assertEqual(request.status_code, 200)

    def test_get_incorrect(self):
        request = self.app.get('/api/employee/3')
        self.assertEqual(request.status_code, 404)

    def test_put_correct(self):
        request = self.app.put('api/employee/1', data={'name': 'Sam Polo', 'department_id': 10001,
                                                       'date_of_birthday': '1998-01-01', 'salary': 2000})
        self.assertEqual(request.json, {'id': '1'})
        self.assertEqual(request.status_code, 201)

    def test_put_incorrect(self):
        # department not found
        request = self.app.put('api/employee/1', data={'name': 'Sam Polo', 'department_id': 10004,
                                                       'date_of_birthday': '1998-01-01', 'salary': 2000})
        self.assertEqual(request.status_code, 400)
        # employee not found
        request = self.app.put('api/employee/5', data={'name': 'Sam Polo', 'department_id': 10001,
                                                       'date_of_birthday': '1998-01-01', 'salary': 2000})
        self.assertEqual(request.status_code, 404)

    def test_delete_correct(self):
        request = self.app.delete('api/employee/1')
        self.assertEqual(request.json, {'id': '1'})
        self.assertEqual(request.status_code, 200)

    def test_delete_incorrect(self):
        request = self.app.delete('api/employee/5')
        self.assertEqual(request.status_code, 404)


if __name__ == '__main__':
    unittest.main()
