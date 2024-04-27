from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server
import os
import re
import Splide from '@splidejs/splide';

app = Flask(__name__)
db = SQL("sqlite:///portfolio.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    db.execute("DROP TABLE projects")
    db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT, type TEXT)")
    # Directory path to search for README files
    directory = '/home/ipsum/vscodespace/'

    # Iterate over files in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower() == 'project.md':
                with open(os.path.join(root, filename), 'r') as file:
                    lines = file.read().splitlines()
                if len(lines) >= 1:
                    name = lines[0].strip()
                else: name = ""
                if len(lines) > 1:    
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
                if len(lines) >= 5:
                    type = lines[4].strip()
                else:
                    type = ""
                db.execute("INSERT INTO projects (name, image, description, link, type) VALUES (?, ?, ?, ?, ?)", name, image, description, link, type)
    c_projects = db.execute("SELECT * FROM projects WHERE type = 'c'")
    py_projects = db.execute("SELECT * FROM projects WHERE type = 'python'")
    web_projects = db.execute("SELECT * FROM projects WHERE type = 'web'")
    other_projects = db.execute("SELECT * FROM projects WHERE type = 'other'")
    return render_template("projects.html", c_projects=c_projects, py_projects=py_projects, web_projects=web_projects, other_projects=other_projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/cali")
def cali():
    return render_template("cali.html")


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()