from flask import Blueprint, render_template, redirect, url_for, request,jsonify
pages = Blueprint("pages", __name__, static_folder="static", template_folder="templates")

@pages.route("/")
def user():
    return render_template("index.html")



#pages for profile

@pages.route("/GDT/Fatima_Hadood_1999-2025")
def one():
    return render_template("/GDT/f.html")

