from flask import render_template, request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario

@app.route( '/users', methods=["GET"] )
def todoUsuarios():
    users = Usuario.obtenerListaUsuarios()
    return render_template( "leer.html", users=users )

@app.route( '/users/new', methods=["GET"] )
def crearUsuario():
    return render_template("crear.html")

@app.route( '/new', methods=["POST"] )
def irCrear():
    return redirect( '/users/new' )

@app.route( '/registro', methods=["POST"] )
def irInicio():
    nuevoUsuario = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "fecha" : request.form["fecha"],
        "fecha" : request.form["fecha"]
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["fecha"] = request.form["fecha"]
    Usuario.agregaUsuario( nuevoUsuario )

    return redirect( '/users' )

@app.route( '/home', methods=["POST"] )
def irMostrar():
    return redirect( '/users' )