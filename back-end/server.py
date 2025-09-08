from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "<h1>Hello, World!</h1>"

@app.route('/homepage')
def hello_world_homepage():
	return "<h1> No </h1>"

@app.route('/actualfile')
def actual_file():
	return render_template("index.html")

app.run(host='0.0.0.0', port='8080', debug=True)
