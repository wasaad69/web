from flask import Flask, render_template
from pages import pages
from lit import lit
from GDT import GDT

app = Flask(__name__)
app.register_blueprint(pages, url_prefix="")
app.register_blueprint(lit, url_prefix="")
app.register_blueprint(GDT, url_prefix="")



if __name__ == "__main__":
    app.run(debug=True)