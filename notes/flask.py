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

fix 404 in app.py:
    @app.route("/")
    def index():
        return render_template("index.html")
        
        
    @app.route("/greet")
    def greet():
        name = request.args.get("name", "world")
        return render_template("greet.html", name=name)
    copy current index.html to greet.html as that is the code u want, but replace the form with:
        hello, {{ name }}

bro but copying code is dumb ?
    create file called layout.hyml in templates/
        copy code from either greet or index.
        remove the content that is not the same on each page
        input:
            {% block body %}{% endblock %} ~ body can be named anything, but its convention to name it what its inside (its jinja syntax)
    inside of index and greet, remove any content that is inside of layout.html and insert this code:
        {% extends "layout.html" %}
        
        {% block body %}
        
            hello, {{ name }} ~ ur code here
        
        {% endblock %}
    
how do i send sensitive info like passwords?
    in app.py:
        @app.route("/greet", methods=["POST"]) ~ you can also include both with methods=["GET", "POST"].
        ~  other types of http requests: delete and put. they are less supported

    in html:
        <form action ="/greet" method="post"> ~ (instead of method="get")
        
    request.args will fail though, because there is no "name" key in it, as its not in the url. to fix this:

    in app.py:
        request.form.get is to be used instead of request.args.get, with the same syntax.

if u want to make a single route support multiple meethods:
    in app.py:
        @app.route("/", methods=["GET", "POST"])
        def index():
            if request.method == "POST":
                name = request.form.get("name", "world")
                return render_template("greet.html", name=name)
            return render_template("index.html")
    
    in html:
        <form method="post"> ~ (/greet doesnt exist anymore, so u can remove the action to return to where u came)
            code
        </form>
    
clicking greet without any text will not use the "world" placeholder, as it is still getting a string, albeit empty. to fix:
    in app.py:
        name = request.form.get("name") ~ remove "world" placeholder
        return render_template("greet.html", name=name)

    in greet.html:
        hello, {% if name %}{{ name }}{% else %}world{% endif %} ~ if name, print name (variable). else print "world".

html dropdown:
<form action="/register" method="post">
    <select name="name">
        <option disabled selected value="">Name</option>
        <option value="Ashlyn">Ashlyn</option>
        <option value="Ashley">Ashley</option>
        <option value="Ashlynn">Ashlynn</option>
    </select>
</form>
    
verify that name is being submitted in app.py:
    @app.route("register", methods=["POST"])
    def register():
        if not request.form.get("name"):
            return render_template("failure.html") ~ assuming that failure.html is a file that exists
        return render_template("success.html")  ~ assuming that success.html is a file that exists
        
how do i make sure its one of the names i have in html?
    in app.py:
    NAMES = ["Ashlyn", "Ashley", "Ashlynn"]
    ...
    return render_template("index.html", names=NAMES)

    in index.html:
        <select name="name">
            {% for name in names %}
                <option value="{{ name }}">{{ name }}</option>
            {% endfor %}
    in app.py: (/register):
    def register():
        if not request.form.get("name") not in NAMES:
            return render_template("failure.html")
        return render_template("success.html")
    
what if im using checkboxes and want to check all values selected?:
in app.py:
    if not request.form.get("name"):
        return render_template("failure.html")
    for name in request.form.getlist("name"):
        if name not in NAMES:
            return render_template("failure.html")
    return render_template("success.html")
    
making an error page:
in error.html:
    {% extends "layout.html" %}
    {% block body %}
        <h1>Error</h1>
        <p>{{ message }}</p>
        <img alt="Grumpy Cat" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZiMzM3cTUxaXR2c29ncHM5Mnk2aHFuOG1xOXUxOTJpaGMxeDR1ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LbGtuww7ZFhgQ/giphy.gif">
    {% endblock %}
"""
