import os



from flask import Flask, session, render_template, request, redirect, flash, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from helpers import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)



# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://kbsgmcmxsiigtq:1b07e5c59561e10e54c6200d58e156b2d34b61e9e77163abb2a6d30f0234e4c8@ec2-34-198-31-223.compute-1.amazonaws.com:5432/d7asutiku5v9h3")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
@login_required
def index():
    session.clear()
    return render_template("login.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Elimina sesion anterior
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # validar que ingreso usuario
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # validar que ingreso password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          {"username":request.form.get("username")}).fetchone()


        # Remember which user has logged in
        session["user_id"] = rows[0]

        # Redirect user to home page
        return render_template("index.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Ingrese un username",400)

        elif not request.form.get("password"):
            return apology("Ingrese un password",400)

        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("Las contraseñas no coinciden",400)

        #Genera la contraseña en hashes para que no se mire la contraseña.
        hash=generate_password_hash(request.form.get("password"))

        validar = db.execute("SELECT username FROM users WHERE username = :usuario", {"usuario":request.form.get("username")}).fetchall()


        if(len(validar) != 0):
            return apology("Username is not available")

        new_user_id = db.execute("INSERT INTO users(username, password) VALUES(:usuario,:contrasenia);",{"usuario":request.form.get("username"), "contrasenia": hash})
        db.commit()

        if not new_user_id:
            return apology("Username ya utilizado",400)
        
       

        flash("Registered was succesful")
        return redirect("/")
    else:
        return render_template("register.html")


    return register

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")