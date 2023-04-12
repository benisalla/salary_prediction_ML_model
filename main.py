import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
modelLR = pickle.load(open('modelLR.pkl', 'rb'))
modelSVM = pickle.load(open('modelSVM.pkl', 'rb'))
modelKNN = pickle.load(open('modelKNN.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = [int(x) for x in request.form.values()]
    input = [np.array(data)]
    pred_LR = modelLR.predict(input)
    pred_SVM = modelSVM.predict(input)
    pred_KNN = modelKNN.predict(input)

    output_RL = round(pred_LR[0], 2)
    output_SVM = round(pred_SVM[0], 2)
    output_KNN = round(pred_KNN[0], 2)

    return render_template('index.html', KNN='${}'.format(output_KNN),SVM='${}'.format(output_SVM),LR='${}'.format(output_RL))


if __name__ == "__main__":
    app.run(debug=True)
