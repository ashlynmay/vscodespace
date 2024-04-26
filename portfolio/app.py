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
    try:
        db.execute("DROP TABLE projects")
    except:
        pass
    try:
        db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT)")
    except:
        pass
    # Directory path to search for README files
    directory = '/home/ipsum/vscodespace/'

    # Iterate over files in the directory and child dirs
    for dirpath, dirnames, filenames in os.walk(directory):
        if 'node_modules' in dirpath or any(x.startswith('node_modules') for x in dirnames):
            if not dirpath.endswith('node_modules'):
                # Include files in the same directory as 'node_modules'
                # Process the files here
                for filename in filenames:
                    if filename.lower() == 'readme.md':
                        # Read the content of the README file
                        try:
                            with open(os.path.join(dirpath, filename), 'r') as file:
                                content = file.read()
                        except FileNotFoundError:
                            # File may have moved or been deleted
                            continue
                        content = re.sub(r"<!--(.*?)-->", r"\1", content, flags=re.DOTALL)
                        lines = content.splitlines()
                        try:
                            name = lines[0].strip()
                        except IndexError:
                            name = ""
                        try:
                            image = lines[1].strip()
                        except IndexError:
                            image = ""
                        try:
                            description = lines[2].strip()
                        except IndexError:
                            description = ""
                        try:
                            link = lines[3].strip()
                        except IndexError:
                            link = ""
                        try:
                            db.execute("INSERT INTO projects (name, image, description, link) VALUES (?, ?, ?, ?)", name, image, description, link)
                        except:
                            pass
        continue
    try:
        projects = db.execute("SELECT * FROM projects")
    except:
        projects = None
    return render_template("past-projects.html", projects=projects)


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()