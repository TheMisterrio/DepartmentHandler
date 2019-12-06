from setuptools import setup
with open("README.md", 'r') as f:
    long_description = f.read()
setup(
    name='Department Handler',
    version='1.0',
    author='Nikita Kapusta',
    author_email='themisterrioo@gmail.com',
    long_description=long_description,
    packages=['department-app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask-sqlalchemy', 'mysql-connector',
    'pylint', 'coverage']
)
