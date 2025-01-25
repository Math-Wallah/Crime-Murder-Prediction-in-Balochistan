# predict_model.py
import joblib
import numpy as np

# Load the trained model
model = joblib.load('murder_rate_predictor.joblib')  # Ensure this file exists in the same directory

def predict_murder_rate(poverty_rate, unemployment_rate, income_inequality, education_level, literacy_rate):
    # Prepare the input features as a 2D array for the model
    features = np.array([[poverty_rate, unemployment_rate, income_inequality, education_level, literacy_rate]])
    prediction = model.predict(features)
    return prediction[0]  # Return the predicted murder rate
