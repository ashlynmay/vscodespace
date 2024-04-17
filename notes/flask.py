""" 
path/route: everything after domain. with route?key=value...
    another alternative to flask is django 

"flask run" will run dynamic websites compared to http-server running static websites.

flask conventional files:
    app.py:
    templates/: includes html, css, and js but it can be put elsewhere.
    requirements.txt: simple file specifying what libraries to install
    static/: usually used for css, images, and js
    
making app.py
    from flask import Flask, render_template, request ~ imports flask
    app = Flask(__name__) ~ tells framework to treat file as web app
        __name__ is the current file name.
    @app.route("/") ~ specifies route for code. default is /
    def index(): ~index can be anything, but its a reasonable default
        return  "hello, world"
    ~ doesnt include any html, simply renders "hello, world" even in page source.
    
    to use html:
        return render_template("index.html")
        
request (from flask import): refers to any http requests
request.args: python dictionary of all key value pairs from url

in html: {{ placeholder }} is defined in jinja as a placeholder value, its normal to name name this what goes in that spot. ex: name.

inside of the app.py file, you can allow the user to input stuff into that placeholder value.
    from flask import Flask, render_template, request
    app = Flask(__name__)
    @app.route("/")
    def index():
        name  = request.args["name"]
        return render_template("index.html", placeholder=name) ~ change placeholder ot whatever is in {{ }}, can even be name=name
now if u manually change url to end with /?name=Ashlyn, the result will be "hello, Ashlyn", with even the source seeming to be that html
if you dont insert that parameter into the url, u get a bad request returned (error code 400), due to placeholder not existing
to fix this, add this code:
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "placeholder"
if no param, will say "hello, placeholder"

it can be simpler and easier to do this instead though:
change "name = request.args["name"] to:
    name = request.args.get("name", "placeholder")        

use html form to change link values:
    <form action="/greet" method ="get"> ~ defines a new route called greet when form is submitted. if no route exists = error 404
        <input autocomplete=off autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet<button>
    
    
"""