from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/mutation')
def get_assay():
	return json.dumps({'Mutation 1':1, 'Mutation 2':2, 'Mutation 3':3})

if __name__ == '__main__':
	app.run()
