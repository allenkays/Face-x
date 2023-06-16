#!/usr/bin/python3

# app/routes.py
import os
from app.database_operations import DatabaseManager
from user_interface import UserInterface
from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
main_routes = Blueprint('main', __name__)
database_url = "mysql+pymysql://facex:Face_x@localhost/face_recognition"


# Create an instance of the UserInterface
database_manager = DatabaseManager(database_url)
user_interface = UserInterface(database_manager)

app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect('/')
    
    file = request.files['file']
    if file.filename == '':
        return redirect('/')

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)

    # Recognize faces in the uploaded image
    recognized_faces = user_interface.recognize_faces(image_path)

    return render_template('results.html', recognized_faces=recognized_faces)


if __name__ == '__main__':
    app.run()