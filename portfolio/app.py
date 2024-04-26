from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server
import os
import re

app = Flask(__name__)
db = SQL("sqlite:///portfolio.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current-projects")
def current_projects():
    return render_template("current-projects.html")

@app.route("/past-projects")
def past_projects():
    db.execute("DROP TABLE projects")
    db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT)")
    # Directory path to search for README files
    directory = '/home/ipsum/vscodespace/'

    # Iterate over files in the directory and child dirs
    for dirpath, dirnames, filenames in os.walk(directory):
        if 'node_modules' in dirpath or any(x.startswith('node_modules') for x in dirnames):
            if not dirpath.endswith('node_modules'):
                # Include files in the same directory as 'node_modules'
                # Process the files here
            continue
        
    projects = db.execute("SELECT * FROM projects")
    return render_template("past-projects.html", projects=projects)



if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()