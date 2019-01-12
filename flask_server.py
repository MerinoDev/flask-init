from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def hello():
	return 'Hello, Juan'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'User name is: ' + request.values['username']
	else:
		return '<form method="POST" action="/login"><input type="text" name="username"><button type="submit">Log in</button></form>'


if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.run(debug=True, port=port, host=host)
