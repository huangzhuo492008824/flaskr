from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, required=True, help='Rate to charge for this resource')

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        args = parser.parse_args()
        rate = args['rate']
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}, 201, {'Etag': 'test----'}

api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)