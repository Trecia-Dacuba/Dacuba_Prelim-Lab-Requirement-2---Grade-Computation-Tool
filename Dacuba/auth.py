from flask import Blueprint

auth = Blueprint('auth','_name_')

@auth.route('/login')
def login():
    return "Login page (authentication not implemented)"