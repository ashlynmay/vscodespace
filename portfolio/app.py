from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from livereload import Server
import os

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
    db.execute("DROP TABLE projects;
    db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT)")
    # Directory path to search for README files
    directory = '/home/ipsum/vscodespace/'

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.lower() == 'readme.md':
            # Read the content of the README file
            with open(os.path.join(directory, filename), 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                image = lines[1].strip()
                if len(lines) >= 3:
                    description = lines[2].strip()
                else:
                    description = ""
                db.execute("INSERT INTO projects (name, image, description) VALUES (?, ?, ?)", name, image, description)
    return render_template("past-projects.html")

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()