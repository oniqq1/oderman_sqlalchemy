from base import *
from flask import render_template, request, redirect, url_for, abort
from flask import Flask
from pizza import Pizzas

app = Flask(__name__)
create_db()


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/pizzas/")
def pizzas():
    with Session() as session:
        data = session.query(Pizzas).all()
    return render_template("pizzas.html",iterable=data)

@app.post("/add_pizzas/")
def pizzas_add():
    name = request.form['name']
    description = request.form['description']
    cost = request.form['cost']

    with Session() as session:
        session.add(Pizzas(name=name,description=description,cost=cost))
        session.commit()
    return render_template("index.html")

@app.get("/add_pizzas/")
def pizzas_add_start():
    return render_template("admin.html")

app.run(port=29998,debug=True)
