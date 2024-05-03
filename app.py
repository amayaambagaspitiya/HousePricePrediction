import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Define the input fields
st.title('House Price Prediction')

st.write('Please enter the following details:')

house_age = st.number_input('House Age', min_value=0, max_value=100, value=50)
ave_rooms = st.number_input('Average Rooms', min_value=0, value=5)
ave_bedrms = st.number_input('Average Bedrooms', min_value=0, value=3)
population = st.number_input('Population', min_value=0, value=1000)
ave_occup = st.number_input('Average Occupation', min_value=0, value=3)
latitude = st.number_input('Latitude', min_value=-90.0, max_value=90.0, value=37.0)
longitude = st.number_input('Longitude', min_value=-180.0, max_value=180.0, value=-122.0)

# Create a DataFrame with the input data
input_data = pd.DataFrame({
    'HouseAge': [house_age],
    'AveRooms': [ave_rooms],
    'AveBedrms': [ave_bedrms],
    'Population': [population],
    'AveOccup': [ave_occup],
    'Latitude': [latitude],
    'Longitude': [longitude]
})

# Load the trained model (you need to replace 'model.pkl' with the path to your trained model file)
model = LinearRegression()  # Assuming you're using a linear regression model
model.load('model.pkl')

# Make predictions
prediction = model.predict(input_data)

# Display the prediction
st.write('Predicted Price:', prediction[0])
