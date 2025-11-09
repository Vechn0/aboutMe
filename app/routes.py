from flask import render_template, request,redirect,url_for

from app import app

@app.route("/")
def main():
    return render_template("index.html")