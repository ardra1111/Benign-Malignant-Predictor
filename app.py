import streamlit as st
import pickle

# Load the trained model (replace 'model.pkl' with your actual filename)
model = pickle.load(open('model.pkl', 'rb'))

# Title for your web app
st.title(' Benign or Malignant Tissue Classification')

# Input fields for features
perimeter_se = st.text_input("Enter Perimeter SE value")
area_se = st.text_input("Enter Area SE value")
radius_worst = st.text_input("Enter Radius Worst value")
compactness_worst = st.text_input("Enter Compactness Worst value")

# Button to make predictions
if st.button("Predict"):
  # Prepare the input data for the model
  try:
    # Data validation and conversion
    perimeter_se = float(perimeter_se.replace(",", "."))  # Replace comma with dot (optional)
    area_se = float(area_se.replace(",", "."))
    radius_worst = float(radius_worst.replace(",", "."))
    compactness_worst = float(compactness_worst.replace(",", "."))

    # Create model input list
    model_input = [perimeter_se, area_se, radius_worst, compactness_worst]

    # Make predictions using the loaded model
    prediction = model.predict([model_input])[0]

    # Display the prediction result
    if prediction == 1:
      st.header("Malignant")
    else:
      st.header("Benign")
  except ValueError:
    st.error("Invalid input. Please enter numbers only.")

