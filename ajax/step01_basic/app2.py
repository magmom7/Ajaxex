from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)   

# client가 요청시에 정수값을 서버에 전송하게 되는 구조의 구성
# server는 client가 전송하는 데이터 획득해서 활용

# http://ip:port/hello/1
@api.route('/hello/<int:id_no>')  # 입력되는 정수값을 id_no 로 받는 parameter 변수 
class HelloWorld(Resource):
    
    # get방식의 요청을 처리하는 메소드 
    def get(self, id_no):
        print('get --------')
        return {"hello":"get"}

    # post방식의 요청을 처리하는 메소드 
    def post(self, id_no):
        print('post --------')
        return {"hello":"post"}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)


'''
1. get 요청 방식과 post 요청 방식 실습으로 습득하기
2. client가 데이터를 입력해서 전송하는 구조로 실습 

'''