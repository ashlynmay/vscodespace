from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current-projects")
def current_projects():
    return render_template("current-projects.html")

@app.route("/past-projects")
def past_projects():
    CREATE 
    return render_template("past-projects.html")

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()