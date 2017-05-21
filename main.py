import logging

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

# Old blog redirect
@ app.route('/2014/09/14/ray-casting-algorithm')
def ray_casting_algorithm_redirect():
    return redirect('/posts/ray-casting-algorithm', code=302)

@app.route('/posts/ray-casting-algorithm')
def ray_casting_algorithm():
    return render_template("ray-casting-algorithm.html")

