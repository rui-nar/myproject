"""Main Server class"""
from flask import Flask
import pymongo

client = pymongo.MongoClient()

from components.userinterface import USER_INTERFACE


APP = Flask(__name__)
APP.register_blueprint(USER_INTERFACE)

if __name__ == '__main__':
    APP.run()
