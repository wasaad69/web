from flask import Blueprint, render_template, redirect, url_for, request
GDT = Blueprint("GDT", __name__, static_folder="static", template_folder="templates")




@GDT.route("/GDT")
def victims():
    return render_template("victims.html")
    
@GDT.route('/1infants')
def content4():
    return render_template("C4GDT/1infants.html")
    
@GDT.route('/2toddlers')
def content3():
    return render_template("C4GDT/2toddlers.html")

@GDT.route('/3children')
def content5():
    return render_template("C4GDT/3children.html")
@GDT.route('/4t')
def content6():
    return render_template("C4GDT/4teenagers.html")

@GDT.route('/5ya')
def content7():
    return render_template("C4GDT/5youngadults.html")
@GDT.route('/6a')
def content8():
    return render_template("C4GDT/6adults.html")
@GDT.route('/7s')
def content9():
    return render_template("C4GDT/7seniors.html")

