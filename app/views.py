from app import app
from flask import render_template, request, redirect, jsonify

@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")
