from flask_restful import Resource
from flask import request, jsonify

class TestRoute(Resource):
    def get(self):
        return "GET Response"
    
    def post(self):
        return "POST Response"