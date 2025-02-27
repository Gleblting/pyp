from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysit.db'
db = SQLAlchemy(app)

class staty(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	intro = db.Column(db.String(300), nullable=False)
	text = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow())



	def __repr__(self):
		return '<staty %r>' % self.id

	db.create_all()

@app.route('/home')
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
	return f"User {name} identity {id}"

if __name__ == "__main__":
	app.run(debug=True)
