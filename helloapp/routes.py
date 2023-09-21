from flask import redirect, url_for, render_template
from helloapp import app


@app.route("/")
def hello():
    return render_template("index.html", title="Title page of Hello App", user=None)


@app.route("/user/<username>")
def hello_user(username):
    return render_template("index.html", title="Title page of Hello App", user=username)


@app.route("/users/")
def display_users():
    users = ['John', 'Rosy', 'Jack', 'Sammy', 'Lilly']
    return render_template('users.html', title='Users', users=users)


@app.route("/user/<username>/<int:age>")
def display_age(username, age):
    return "Hello " + username + "!!!<br>You are " + str(age) + " years old."


@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")


@app.route("/greet/user/<uname>")
def greet_user(uname):
    return redirect(url_for('hello_user', username=uname))
