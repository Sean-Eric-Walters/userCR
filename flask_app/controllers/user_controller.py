from flask import Flask, render_template, request, session, redirect

from flask_app import app
from ..models.user import User


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