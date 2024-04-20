import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide stock symbol and the amount of shares", 402)
        elif lookup(request.form.get("symbol")) == None:
            return apology("stock not found", 402)
#            result = lookup(request.form.get("symbol"))
#            return render_template("quoted.html", symbol=result["symbol"], price=result["price"])
        elif request.form.get("shares") < 1:
            return apology("you cannot purchase less than 1 share", 402)
        else:
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            price = (lookup(request.form.get("symbol"))["price"])
            if cash-(price*shares) > 0:
                if db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='purchases'"):
                    db.execute("INSERT INTO purchases (id, stock, shares, price, total)")
                else:
            else:
                return apology("not enough funds to complete purchase", 402)
            
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if lookup(request.form.get("symbol")) != None:
            result = lookup(request.form.get("symbol"))
            return render_template("quoted.html", symbol=result["symbol"], price=result["price"])
        else:
            return apology("stock not found", 402)
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted and confirmed
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide and confirm password", 403)
        
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords provided do not match", 403)

        # Ensure username does not exist and create a new account.
        elif len(db.execute("SELECT username FROM users WHERE username = ?", (request.form.get("username"), ))) == 0:
            hpswd = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash, cash) VALUES (?, ?, 0)", request.form.get("username"), hpswd)
            uid_result = db.execute("SELECT id FROM users WHERE username = ?", (request.form.get("username"),))
            # Log into newly created account.
            if uid_result:
                 uid = uid_result[0]["id"]
                 session["user_id"] = uid
            return redirect("/")
        elif len(db.execute("SELECT username FROM users WHERE username IS ?", (request.form.get("username"), ))) > 0:
            return apology("username already taken", 403)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
