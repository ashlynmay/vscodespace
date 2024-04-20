import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
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
    stock = db.execute("SELECT stock FROM purchases WHERE id = ?", session["user_id"])
    shares = db.execute("SELECT stock, shares FROM purchases WHERE id = ?", session["user_id"])
    purchased = db.execute("SELECT price FROM purchases WHERE id = ?", )
    cash_result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash_result[0]["cash"] if cash_result else 0

    total = cash + 
    prices = []
    for entry in stock:
        stock_price = lookup(entry["stock"])["price"]
        prices.append(stock_price) 
        shares_for_stock = next((share["shares"] for share in shares if share["stock"] == entry["stock"]), 0)
        total_value = (stock_price * shares_for_stock)
        total += total_value
    combined_data = [{"stock": entry["stock"], "shares": shares_for_stock["shares"], "price": stock_price, "total_value": stock_price * shares_for_stock["shares"]} for entry, shares_for_stock, stock_price in zip(stock, shares, prices)]


    return render_template("index.html", combined_data=combined_data, total=cash)


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
        elif int(request.form.get("shares")) < 1:
            return apology("you cannot purchase less than 1 share", 402)
        else:
            cash_result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            cash = cash_result[0]["cash"] if cash_result else 0
            price = (lookup(request.form.get("symbol"))["price"])
            shares = (request.form.get("shares"))
            stock = str(request.form.get("symbol"))
            stock = stock.upper()
            total = float(price) * int(shares)
            newcash = cash - int(total)
            if cash - total > 0:
                current_datetime = datetime.now()
                if not db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='purchases'"):
                    db.execute("CREATE TABLE purchases (id INTEGER NOT NULL, stock TEXT NOT NULL, shares INTEGER NOT NULL, price NUMERIC NOT NULL, total NUMERIC NOT NULL)")
                if not db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history'"):
                    db.execute("CREATE TABLE history (id INTEGER NOT NULL, stock TEXT NOT NULL, shares INTEGER NOT NULL, price NUMERIC NOT NULL, total NUMERIC NOT NULL, type TEXT NOT NULL, dt DATETIME)")

                existing_shares = db.execute("SELECT shares FROM purchases WHERE stock = ? AND id = ?", stock, session["user_id"])
                existing_total = db.execute("SELECT total FROM purchases WHERE stock = ? AND id = ?", stock, session["user_id"])
                existing_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                if existing_shares:
                    existing_shares_int = existing_shares[0]["shares"]
                    updated_shares = existing_shares_int + int(shares)  # Convert shares to an integer
                
                if existing_cash:
                    existing_cash_int = existing_cash[0]["cash"]
                    updated_cash = existing_cash_int - int(total)
                
                if existing_total:
                    existing_total_int = existing_total[0]["total"]
                    updated_total = existing_total_int + int(total)  # Convert shares to an integer
                    
                    
                    db.execute("UPDATE purchases SET shares = ?, total = ? WHERE stock = ? AND id = ?", updated_shares, updated_total, stock, session["user_id"])
                    db.execute("INSERT INTO history (id, stock, shares, price, total, type, dt) VALUES (?, ?, ?, ?, ?, 'BUY', ?)", session["user_id"], stock, int(shares), price, total, current_datetime)
                    db.execute("UPDATE users SET cash = ?", updated_cash)
                else:
                    db.execute("INSERT INTO purchases (id, stock, shares, price, total) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock, int(shares), price, total)
                    db.execute("INSERT INTO history (id, stock, shares, price, total, type, dt) VALUES (?, ?, ?, ?, ?, 'BUY', ?)", session["user_id"], stock, int(shares), price, total, current_datetime)
                    db.execute("UPDATE users SET cash = ?", newcash)
                return redirect("/")
            else:
                return apology("not enough funds to complete purchase", 402)
        
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM history WHERE id = ? ORDER BY dt DESC", session["user_id"])
    return render_template("history.html", history = history)


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
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), hpswd)
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
    if request.method == "POST":
        stock = request.form.get("symbol")
        stock = stock.upper()
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide stock symbol and the amount of shares", 402)
        elif lookup(stock) == None:
            return apology("stock not found", 402)
        elif int(request.form.get("shares")) < 1:
            return apology("you cant sell less than 1 share", 402)
        share_result = db.execute("SELECT shares FROM purchases WHERE id = ? AND stock = ?", session["user_id"], stock)
        if share_result:
            shares = share_result[0]["shares"]
        else:
            shares = 0
        updated_shares = shares - int(request.form.get("shares"))
        total_result = db.execute("SELECT total FROM purchases WHERE id = ? AND stock = ?", session["user_id"], stock)
        total = total_result[0]["total"]
        price = lookup(stock)["price"]
        ntotal = int(request.form.get("shares")) * price
        updated_total = total - ntotal
        current_datetime = datetime.now()
        if int(request.form.get("shares")) > shares:
            return apology("you dont have that many shares to sell", 402)
        else:
            db.execute("UPDATE purchases SET shares = ?, total = ? WHERE stock = ? AND id = ?", updated_shares, updated_total, stock, session["user_id"])
            db.execute("INSERT INTO history (stock, shares, price, total, type, dt, id) VALUES (?, ?, ?, ?, 'SELL', ?, ?)", stock, request.form.get("shares"), price, ntotal, current_datetime, session["user_id"])
            return redirect("/")
    else: return render_template("sell.html")