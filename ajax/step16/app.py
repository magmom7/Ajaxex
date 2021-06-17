from flask import Flask, request, render_template
from dao import EmpDAO

app = Flask(__name__)


# http://127.0.0.1:5000   -> http://127.0.0.1:5000/ 동일한 표현
# method속성 생략시 get 방식
@app.route("/", methods=["get"])
def get():
    print("get")
    # http://127.0.0.1:5000/resque.html url 의미
    return render_template("reqres.html")


@app.route("/getdata", methods=["get"])
def getdata():
    print("getdata()------------")
    return '{"name":"재석", "age":49}'


@app.route("/getemp", methods=["post"])
def datemp():
    return EmpDAO().empone(request.form.get('empno'))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
