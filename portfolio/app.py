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

<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
@app.route("/past-projects")
def past_projects():
    db.execute("DROP TABLE projects")
    db.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, image TEXT, link TEXT)")
    # Directory path to search for README files
    directory = '/home/ipsum/vscodespace/'

    # Iterate over files in the directory and child dirs
    for dirpath, dirnames, filenames in os.walk(directory):
+        if 'nord_modules' in dirpath or any(x.startswith('nord_modules') for x in dirnames):
-        if 'nord_modules' in dirpath:
            continue
        for filename in filenames:
            if filename.lower() == 'readme.md':
                # Read the content of the README file
                with open(os.path.join(dirpath, filename), 'r') as file:
                    content = file.read()
                    content = re.sub(r"<!--(.*?)-->", r"\1", content, flags=re.DOTALL)
                    lines = content.splitlines()
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
<<<<<<<  f326a368-2d22-4b31-838f-0b7454d75982  >>>>>>>



if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()