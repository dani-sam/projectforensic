from flask import *

public = Blueprint('public',__name__)


@public.route('/')
def publicHome():
    return render_template('public_pages/publicHome.html')

@public.route('/home')
def home():
    return render_template('public_pages/publicHome.html')

@public.route('/login')
def login():
    return render_template('public_pages/login.html')