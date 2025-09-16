from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
	if request.method == 'POST':
		data = request.form['version']
	return render_template("./home-page/index.html", version=data)

@app.route('/login')
def login():
	return render_template("./login/index.html", version='4')

@app.route('/register')
def register():
	return render_template("./register/index.html", version='4')

app.run(host='0.0.0.0', port='8080', debug=True)
