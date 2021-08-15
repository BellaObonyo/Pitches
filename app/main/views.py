from flask import render_template,request,redirect,url_for
from . import main
from ..models import 

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index page and its data
	'''
	

	return render_template('index.html')




