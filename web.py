from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
# @cross_origin()
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        time_spend_company = float(request.form["time_spend_company"])
        init_features = [float(x) for x in request.form.values()]
        x = [np.array(init_features)]
        ml = model.predict(x)

    

        if ml == 1:
            k = ml-time_spend_company
        
            if k<=0:
                t="immediately"
            else:
                k = k.item()
                k = round(k, 1)
                t="within "+ str(k) + " years" 
            return render_template('index.html', result='The Employee is more likely to Leave the Organization {}!'.format(t))
            



        else:
            g = "continue in"
            return render_template('index.html', result='The Employee is more likely to {} the Organization!'.format(g))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)
    app.run(debug=True)

