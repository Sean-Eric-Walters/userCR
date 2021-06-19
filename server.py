from flask import Flask, render_template, request, session, redirect

from user import User


app = Flask(__name__) 
app.secret_key = "see no evil, speak no evil, hear no evil"


@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("index.html", all_users = users)


@app.route("/user/new")
def create_user_form():
    return render_template("create.html")

@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)

    return redirect("/")


if __name__=="__main__":     
    app.run(debug=True) 