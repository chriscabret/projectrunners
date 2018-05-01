from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('freelancer.css')

@app.route('/<name>')
def profile(name):
	return render_template('freelancer.css', name=name)



if __name__ == '__main__':
	app.run(debug=True)
