from flask import Blueprint, render_template, redirect, url_for, request
lit = Blueprint("lit", __name__, static_folder="static", template_folder="templates")

    
@lit.route('/crimes')
def crime():
    return render_template('crime.html')
    
@lit.route('/content1')
def content1():
    return '<h2>Content 1</h2><p class="ste">This is the first content.</p><img src="static/2.jpg">'
    
@lit.route('/content2')
def content2():
    return '<h2>Content 2</h2><p>This is the second content.</p>'