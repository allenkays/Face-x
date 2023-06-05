#!/usr/bin/python3

from flask import Flask, render_template
from  ui.routes import main_routes

app = Flask(__name__)
app.register_blueprint(main_routes)


if __name__ == '__main__':
    app.run()