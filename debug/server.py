from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def actual_file():
	return render_template("./home-page/index.html", version='4')

app.run(host='0.0.0.0', port='8080', debug=True)
