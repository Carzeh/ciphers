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
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)

    cmd_args = parser.parse_args()
    app_options = {"port": cmd_args.port }

    if cmd_args.debug_mode:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False
    app.run(**app_options)