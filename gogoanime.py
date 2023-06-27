from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
	query = request.args.get('query')
	res = requests.get("https://api.cosumet.org/gogoanime/","query")
	print(res.text)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, use_reloader=True, threaded=True)