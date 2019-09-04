# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:51:42 2019

@author: GS-1854
"""
from flask import Flask
from .Data_Generation import face_database
from .Detection_Algorithm import facial_recognition

app = Flask(__name__)

@app.route('/')
def face_authentication():
    print("Welcome")
    return "Welcome to face authentication system"

@app.route('/data_generate')
def create_face_data(directory, user_name):
    face_detection = face_database(directory, user_name)
    if face_detection == "Success":
        return "Success"
    return "failure"

@app.route('/face_verification')
def face_recognition(directory, user_name):
    face_recognize = facial_recognition(directory)
    if face_recognize == "Success":
        return "Success"
    return "not recognized"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
