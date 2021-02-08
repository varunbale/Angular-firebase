from flask import Flask, render_template
from flask_cors import CORS


import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate("F:\key.json")
firebase_admin.initialize_app(cred)




app=Flask(__name__)
CORS(app)

from api import user_info

app.register_blueprint(user_info, url_prefix='/api')

@app.route('/')
def index():
    return "index"

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)    