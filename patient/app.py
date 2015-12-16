from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/patient')
def get_assay():
	return json.dumps({1:"John Snow", 2:"Ned Stark", 3:"Tyrion Lannister"})

if __name__ == '__main__':
	app.run()
