from flask import render_template

def register():
    return render_template("register.html", title="Registro de Usuario")

def login():
    return render_template("login.html", title="Inicio de Sesión")
