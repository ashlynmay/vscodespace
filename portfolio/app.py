from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()