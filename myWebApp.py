from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
	html = 	"<h3> Hi Verizon Team !</h3> <b> Hostname : </b> {hostname}<br/>"
	return html.format(hostname=socket.gethostname())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)