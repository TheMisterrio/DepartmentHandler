"""Creates Flask app and initializes logger"""
import logging
from flask import Flask

app = Flask(__name__)
# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler('web-app.log')
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
logger.info('Web-app started')

if __name__ == '__main__':
    app.run(debug=True)
