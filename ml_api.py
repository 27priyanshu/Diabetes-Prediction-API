from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()


class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFuncion: float
    Age: int

# loading the saved model 

diabetes_model = pickle.load(open("diabetes_model.sav","rb"))

@app.post("/diabetes_prediction")
def diabetes_pred(input_parameters:model_input):
    input_data  = input_parameters.json()
    input_dictionary =  json.loads(input_data) 

    # convert dictionary into list

    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFuncion']
    age = input_dictionary['Age']
   
   # final list
    input_list= [preg,glu,bp, skin, insulin, bmi, dpf, age]

    # prediction

    prediction = diabetes_model.predict([input_list])

    if prediction[0 ] == 1:
        return 'The Person is Diabetic'
    else:
        return 'The Person is not Diabetic'
