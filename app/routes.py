from flask import render_template, request, redirect, url_for,flash

from app import app


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact(methods=["GET","POST"]):
    if request.method == "Get":
        return redirect(url_for("index"))
    else:
        name=request.form.get("name")
        email=request.form.get("email")
        surname=request.form.get("surname")
        age=request.form.get("age")
        flash('Данные успешно отправлены')
        return redirect(url_for("contact"))
