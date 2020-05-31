import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")



@app.route("/")
@login_required
def index():
    transactions = db.execute("SELECT (symbol, name, price, shares, total) FROM transactions WHERE ID=(:iD)", iD=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id=(:userid)", userid=session["user_id"])
    return render_template("index.html", transactions=transactions, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = (request.form.get("symbol"))
        shares = request.form.get("shares")

        if shares <= 0 or not lookup(symbol):
            return apology("Please put a value for both symbol and shares")
        else:
            price = lookup(symbol)["price"]
            cash = db.execute("SELECT cash FROM users WHERE id=(:userid)", userid = session["user_id"])
            total = -price * shares
            if total > cash:
                return apology("Not enough money oops", 403)


            db.execute("INSERT INTO transactions (ID, symbol, name, price, shares, total) VALUE (:iD, :symbol, :name, :price, :shares, :total)"
                , iD=session["user_id"], symbol=symbol, name=lookup(symbol)["name"], price=price, shares=shares, total=total)
            db.execute("UPDATE users SET cash=(:newcash) WHERE id=(:userid)", cash=cash+total, userid=session["user_id"])
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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please print a Symbol", 403)
        else:
            return render_template("quoted.html", symbol=lookup(symbol))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        checks = db.execute("SELECT username FROM users WHERE username = (:name)", name=username)

        if not username or not password or not confirmation:
            return apology("Please enter a value for all criterea", 403)
        elif checks:
            return apology("Username already exists", 403)
        elif password != confirmation:
            return apology("Password and condirmation do not match", 403)
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (:name, :thash)",
                name=username, thash = generate_password_hash(password))
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        stocksowned = db.execute("SELECT (symbols, shares) FROM transactions WHERE ID=(:userid)" userid=session["user_id"])
        return render_template("sell.html", stocksowned)
    else:
        symbol = request.form.get("symbol")
        number = request.form.get("shares")
        addedcash = number * lookup(symbol)["price"]
        
        currentnum = db.execute("SELECT shares FROM transactions WHERE ID=(:userid) AND symbol=(:symbol)", userid=session["user_id", symbol=symbol)
        
        if not symbol or currentnum < number or number <= 0:
            return apology("There was an error in precessing", 403)
        
        else:
            db.execute("INSERT INTO transactions (ID, symbol, name, price, shares, total) VALUE (:iD, :symbol, :name, :price, :shares, :total)"
                , iD=session["user_id"], symbol=symbol, name=lookup(symbol)["name"], price=lookup(symbol)["price"], shares=shares, total=addedcash")
            db.execute("UPDATE users SET cash=(:newcash) WHERE id=(:userid)", cash=cash+addedcash, userid=session["user_id"])
        
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
