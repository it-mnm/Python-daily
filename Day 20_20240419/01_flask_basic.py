# Flask 모듈 사용하기
# 터미널에 $env:FLASK_APP="01_flask_basic" 입력
# flask run 입력하면 127.0.0.1:5000 나옴

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>HelloWorld!</h1>"