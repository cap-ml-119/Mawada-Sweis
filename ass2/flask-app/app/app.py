# this file contain flask app
from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Create flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("app/model.sav", "rb"))


# endpoint for predict sample
@app.route("/api/v1/predict/sample", methods=["POST"])
def sample_predict():
    json = request.json
    query_df = pd.DataFrame(json)
    prediction = model.predict(query_df)
    return jsonify({"prediction": list(prediction)})


# @app.route('/api/v1/preduction/batch', methods=['POST'])
# def batch_preduction():


def return_app():
    return app
