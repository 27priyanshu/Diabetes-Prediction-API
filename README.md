# Diabetes Prediction API

The **Diabetes Prediction API** is a machine learning-based API designed to predict whether a person is diabetic based on various health metrics. The model used is a Support Vector Machine (SVM) with an accuracy of 77.27%. The API is developed using FastAPI and deployed on Render.

## Deployed Model

- **API Endpoint**: [https://dibetes-api.onrender.com/diabetes_prediction](https://dibetes-api.onrender.com/diabetes_prediction)

## Usage

### Input

The API expects a JSON object with the following fields:

- `Pregnancies`: Number of times pregnant (integer)
- `Glucose`: Plasma glucose concentration (integer)
- `BloodPressure`: Diastolic blood pressure (integer)
- `SkinThickness`: Triceps skin fold thickness (integer)
- `Insulin`: 2-Hour serum insulin (integer)
- `BMI`: Body mass index (float)
- `DiabetesPedigreeFunction`: Diabetes pedigree function (float)
- `Age`: Age in years (integer)

### Output

The API will return a JSON object with the prediction:

- `"The Person is Diabetic"` if the person is predicted to be diabetic.
- `"The Person is not Diabetic"` if the person is predicted to be non-diabetic.

### Example Requests

#### Test Case 1

**Input**:
```json
{
    "Pregnancies": 10,
    "Glucose": 168,
    "BloodPressure": 74,
    "SkinThickness": 0,
    "Insulin": 0,
    "BMI": 38,
    "DiabetesPedigreeFuncion": 0.537,
    "Age": 30
}
```

**Result**:
```json
"The Person is Diabetic"
```

#### Test Case 2

**Input**:
```json
{
    "Pregnancies": 1,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFuncion": 0.351,
    "Age": 31
}
```

**Result**:
```json
"The Person is not Diabetic"
```

## API Testing

You can test the API using tools like [Postman](https://www.postman.com/). Here is how you can do it:

1. Open Postman.
2. Create a new POST request.
3. Set the URL to [https://dibetes-api.onrender.com/diabetes_prediction](https://dibetes-api.onrender.com/diabetes_prediction).
4. In the Body tab, select `raw` and `JSON` format.
5. Enter the JSON object as per the input format.
6. Send the request and check the response.

## Conclusion

This Diabetes Prediction API provides an easy and efficient way to predict diabetes using health metrics. With an accuracy of 77.27%, it can be a valuable tool in preliminary health assessments.
