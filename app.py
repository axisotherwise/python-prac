from flask import Flask, render_template

# 플라스크 객체 인스턴스 생성
app = Flask(__name__)

# 라우터
# def === function
@app.route("/")
def index():
  return "here"

@app.route("/user")
def userRender():
  return render_template("index.html")

# server listen
if __name__ == '__main__':
  app.run(
    port = "2000",
    debug = True
  )