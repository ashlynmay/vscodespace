from hashlib import new
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server
import os
import re

app = Flask(__name__)
db = SQL("sqlite:///portfolio.db")
directory = '/home/ipsum/vscodespace/'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    db.execute("DROP TABLE projects")
    db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT, type TEXT, featured BOOLEAN)")

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
                if len(lines) >= 6:
                    featured = lines[5].strip()
                else:
                    featured = "0"
                db.execute("INSERT INTO projects (name, image, description, link, type, featured) VALUES (?, ?, ?, ?, ?, ?)", name, image, description, link, type, featured)
    featured_c_projects = db.execute("SELECT * FROM projects WHERE type = 'c' AND featured = '1'")
    featured_py_projects = db.execute("SELECT * FROM projects WHERE type = 'python' AND featured = '1'")
    featured_web_projects = db.execute("SELECT * FROM projects WHERE type = 'web' AND featured = '1'")
    featured_other_projects = db.execute("SELECT * FROM projects WHERE type = 'other' AND featured = '1'")
    return render_template("projects.html", c_projects=featured_c_projects, py_projects=featured_py_projects, web_projects=featured_web_projects, other_projects=featured_other_projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/cali")
def cali():
    return render_template("cali.html")

@app.route("/c-projects")
def c_projects():
    if not db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'"):
        db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT, type TEXT, featured BOOLEAN)")
    else:
        projects = db.execute("SELECT * FROM projects WHERE type = 'c'")
        return render_template("c-projects.html", projects=projects)
        


@app.route("/py-projects")
def pyprojects():
    return render_template("py-projects.html")

@app.route("/web-projects")
def webprojects():
    return render_template("web-projects.html")

@app.route("/other-projects")
def otherprojects():
    return render_template("other-projects.html")


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()