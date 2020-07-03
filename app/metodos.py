from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'get world'}
    
    def post(self):
        return {'hello': 'post world'}