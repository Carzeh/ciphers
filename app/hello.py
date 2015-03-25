from flask import Flask
from flask import render_template
from flask import request
import otp as OTP
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/otp', methods=['POST'])
def otp():
	encryption_object = OTP.encrypt(request.form['otp'])
	return json.dumps(encryption_object)

if __name__ == '__main__':
    app.run()