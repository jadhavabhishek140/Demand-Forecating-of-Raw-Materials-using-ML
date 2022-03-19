# from crypt import methods
import pandas as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
steel_model = pickle.load(open('steel_model.pkl', 'rb'))
plastics_model = pickle.load(open('plastics_model.pkl', 'rb'))
iron_model = pickle.load(open('iron_model.pkl', 'rb'))
aluminium_model = pickle.load(open('aluminium_model.pkl', 'rb'))
rubber_model = pickle.load(open('rubber_model.pkl', 'rb'))
glass_model = pickle.load(open('glass_model.pkl', 'rb'))
copper_model = pickle.load(open('copper_model.pkl', 'rb'))

@app.route('/')
def home():
       return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":

        result1 = request.form['startyear']
        result2 = request.form['endyear']
        result3 = request.form['no_of_cars']

        steel = steel_model.predict([[result3]])
        plastics = plastics_model.predict([[result3]])
        iron = iron_model.predict([[result3]])
        rubber = rubber_model.predict([[result3]])
        aluminium = aluminium_model.predict([[result3]])
        glass = glass_model.predict([[result3]])
        copper = copper_model.predict([[result3]])

        steel_output = steel[0][0].round(2)
        plastics_output = plastics[0][0].round(2)
        iron_output = iron[0][0].round(2)
        rubber_output = rubber[0][0].round(2)
        aluminium_output = aluminium[0][0].round(2)
        glass_output = glass[0][0].round(2)
        copper_output = copper[0][0].round(2)

        return render_template("index.html", result1=result1, result2=result2,
                               steel='Quantity of steel is {} tonnes'.format(steel_output),
                               plastics='Quantity of plastics is {} tonnes'.format(plastics_output),
                               iron='Quantity of iron is {} tonnes'.format(iron_output),
                               rubber='Quantity of rubber is {} tonnes'.format(rubber_output),
                               aluminium='Quantity of aluminum is {} tonnes'.format(aluminium_output),
                               glass='Quantity of glass is {} tonnes'.format(glass_output),
                               copper='Quantity of copper is {} tonnes'.format(copper_output))

if __name__ == '__main__':
   app.run(debug=True)