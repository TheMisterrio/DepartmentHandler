"""Starts web app"""
from app import app
import views.view


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5001')
