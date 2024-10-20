import os

from flask import Flask, request

from hairloss_predictor import HairlossPredictor

app = Flask(__name__)
app.config["DEBUG"] = True

# Set the model path using the MODEL_REPO environment variable
model_path = os.path.join(os.getenv('MODEL_REPO', '/usr/src/myapp'), 'model.joblib')

# Initialize the predictor with the model file
dp = HairlossPredictor(model_file=model_path)


@app.route('/hairloss_predictor/', methods=['POST']) # path of the endpoint. Except only HTTP POST request
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_inout = request.get_json()
    return dp.predict_single_record(prediction_inout)

# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)

