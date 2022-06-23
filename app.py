from flask import Flask, render_template, url_for, session, request, redirect

import pymysql

conn = pymysql.connect(
  host = "localhost",
  user = "root",
  password = "axisotherwise",
  db = "python",
  charset = "utf8"
)
curs = conn.cursor()
getUsers = "SELECT * FROM users"
insertUser = "INSERT INTO users (email, password) VALUES (%s, %s)"

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def indexRender():
  if "email" in session:
    return render_template("index.html", email = session.get("email"), login = True)
  else:
    curs.execute(getUsers)
    rows = curs.fetchall()
    return render_template("index.html", login = False)

@app.route("/join", methods = ["get", "post"])
def authJoin():
  if request.method == "GET":
    return render_template("join.html")
  else:
    reqEmail = request.form["email"]
    reqPassword = request.form["password"]
    curs.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (reqEmail, reqPassword))
    conn.commit()
    print("success")
    return redirect("/")
    
@app.route("/login", methods = ["post"])
def authLogin():
  reqEmail = request.form["email"]
  reqPassword = request.form["password"]
  result = curs.execute("SELECT * FROM users WHERE email = (%s)", (reqEmail))
  if result:
    session["email"] = reqEmail
    return render_template("index.html", email = session.get("email"), login = True)
  else:
    return redirect("/")
  
@app.route("/logout", methods = ["delete"])
def authLogout():
  session.pop("email")
  return redirect("/")

if __name__ == "__main__":
  app.run(debug = True)
