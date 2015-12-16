from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/assay')
def get_assay():
	return json.dumps({'Assay 1':1, 'Assay 2':2, 'Assay 3':3})

if __name__ == '__main__':
	app.run()
