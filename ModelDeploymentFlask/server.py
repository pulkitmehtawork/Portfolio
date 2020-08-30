# import libraries
import numpy as np
from flask import Flask , request, jsonify
import pickle

app = Flask(__name__)

# Load the model 
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods = ['POST'])
def predict():
    #get data from post requests
    data = request.get_json()
    # prediction 
    prediction  =  model.predict([[np.array(data['exp'])]])

    # take first value of prediction
    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run(port = 5000,debug = True)


