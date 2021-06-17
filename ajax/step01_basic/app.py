from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)   # swagger doc 개발 API

# http://ip:port/hello
# http://127.0.0.1:80/hello
# http://127.0.0.1/hello
@api.route('/hello')
class HelloWorld(Resource):
    # get방식의 요청을 처리하는 메소드 
    def get(self):
        return {"hello":"world"}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)