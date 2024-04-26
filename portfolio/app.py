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

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.lower() == 'project.md':
            # Read the content of the README file
            with open(os.path.join(directory, filename), 'r') as file:
                lines = file.splitlines()
                if len(lines) >= 1:
                    name = lines[0].strip()
                else: name = ""
                if len(lines) >- 2:    
                    image = lines[1].strip()
                else: image = ""
                if len(lines) >= 3:
                    description = lines[2].strip()
                else:
                    description = ""
                if len(lines) >= 4:
                    link = lines[3].strip()
                else:
                    link = ""
                db.execute("INSERT INTO projects (name, image, description, link) VALUES (?, ?, ?, ?)", name, image, description, link)
    projects = db.execute("SELECT * FROM projects")
    return render_template("past-projects.html", projects=projects)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()