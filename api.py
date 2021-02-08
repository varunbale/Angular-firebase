from flask import Blueprint, render_template, abort, request
import json
from firebase_admin import firestore
db = firestore.client() 

user_info = Blueprint('user_info', __name__)

@user_info.route('/user', methods=['POST'])
def store_user_info():
    user_info=request.json
    db.collection("Florida").document("varun").set(user_info)
    return json.dumps({
        "status":"ok"
    })

   