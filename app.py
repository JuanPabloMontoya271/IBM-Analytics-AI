from flask import Flask, jsonify, request
import json
from gpt3 import DataSloth

import os
from dotenv import load_dotenv
app = Flask(__name__)


sloth = DataSloth(os.getenv("OPENAI"))
@app.route('/')
def index():
    return '<h1>Hello from monty</h2>'


@app.route('/query', methods = ["POST"])
def query():

    prompt = request.json['prompt']
    response, sql_query = (sloth.query(prompt))
    columns = response.columns
    response = json.loads(response.to_json(orient="records"))

    response = {"rows" : response, "columns":list(columns), "query":sql_query }
    return jsonify(response)

@app.route('/qa', methods = ["POST"])
def qa():

    prompt = request.json['prompt']
    response = (sloth.qa(prompt))
    

    return jsonify({"response": response})
    
    

if __name__ == "__main__":
    app.run(debug=True)