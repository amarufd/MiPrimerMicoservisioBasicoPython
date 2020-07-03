from app import app, api
from flask_restful import Resource
from app.metodos import *

api.add_resource(HelloWorld, '/')
