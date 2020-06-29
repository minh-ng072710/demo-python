from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "Hello": "World"
        }


paragraph = """This is line 1
This is line 2
This is line 3"""


test = "                              nguyễn gia           minh       "
print(test.strip())
api.add_resource(HelloWorld, '/')
if __name__ == "__main__":
    app.run(debug=True)
