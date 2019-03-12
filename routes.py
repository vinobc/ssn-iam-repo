from flask import Flask, render_template
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/ssnim'
db.init_app(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/test")
def test():
	return render_template("test.html")

if __name__ == '__main__':
	app.run(debug=True)
