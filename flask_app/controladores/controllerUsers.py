from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.modelos.modelUsers import Users
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )

@app.route( '/', methods=['GET'] )
def homepage():
    return render_template( "login.html" )


@app.route( '/register', methods=["POST"] )
def registerUser():
    if not Users.verifyUser( request.form ):
        return redirect( '/' )

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash( request.form["password"] ),
        "created_at" : datetime.today(),
        "updated_at" : datetime.today()
    }

    idUser = Users.addUser( data )
    if idUser == False:
        flash( "Problemas con el database", "register" )
        return redirect('/')

    session["id"] = idUser
    session["first_name"] = request.form["first_name"]
    return redirect( '/dashboard' )


@app.route( '/login', methods=["POST"] )
def loginUser():
    data = { 
        "email" : request.form["emailUser"] 
        }
    user = Users.getUser( data )
    if not user:
        flash( "E-mail no registrado", "login" )
        return redirect( '/' )

    if not bcrypt.check_password_hash( user["password"], request.form['passwordUser'] ):
        flash( "Contraseña inválida", "login" )
        return redirect( '/' )

    session["id"] = user["id"]
    session["first_name"] = user["first_name"]
    return redirect( "/dashboard" )


@app.route( '/logout', methods=["POST"] )
def deleteSession():
    session.clear()
    return redirect( '/' )