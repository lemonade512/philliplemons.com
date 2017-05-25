import logging

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/posts/no-cheating-allowed')
def no_cheating_allowed():
    return render_template("no-cheating-allowed.html")

@app.route('/posts/ray-casting-algorithm')
def ray_casting_algorithm():
    return render_template("ray-casting-algorithm.html")

##########################################################
#                 Old Blog Redirects                     #
##########################################################
@app.route('/2014/09/14/ray-casting-algorithm')
def ray_casting_algorithm_redirect():
    return redirect('/posts/ray-casting-algorithm', code=302)

@app.route('/2015/08/18/no-cheating-allowed')
def no_cheating_allowed_redirect():
    return redirect('/posts/no-cheating-allowed', code=302)


