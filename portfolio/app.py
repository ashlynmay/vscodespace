from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from app import app
from livereload import Server

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")