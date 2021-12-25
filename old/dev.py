import logging

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/dev/easeljs')
def about():
    return render_template("easeljs.html")
