import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('waste_model.h5')

# Function to preprocess the image for prediction
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image to the input size expected by the model
    img_array = np.array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch size
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Function to predict the category of the image
def predict_category(img):
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)  # Get the index of the predicted class
    class_labels = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
                    'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
    return class_labels[class_idx[0]], prediction[0][class_idx[0]]

# Streamlit UI setup
st.set_page_config(page_title="Waste Classification Demo", page_icon=":recycle:", layout="wide")
st.title("Waste Classification Demo with our Trained AI Model")

# Sidebar: Upload Images
st.sidebar.header("Upload Images")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Add a message below the file uploader
st.sidebar.write("Please upload pictures for the following categories:")
categories = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
              'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
st.sidebar.write(", ".join([category.capitalize() for category in categories]))

# Show preview and confirmation for a single uploaded file
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    # Display preview of the uploaded image
    st.image(img, caption="Preview of the uploaded image", use_container_width=True)

    # Add a confirmation button
    if st.button("Confirm Upload"):
        # Predict the category after confirmation
        category, confidence = predict_category(img)

        # Display prediction result
        st.success(f"Predicted Category: {category.capitalize()}")
        st.write(f"Confidence: {confidence:.2f}")
    else:
        st.warning("Please confirm the upload to proceed.")
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('waste_model.h5')

# Function to preprocess the image for prediction
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image to the input size expected by the model
    img_array = np.array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch size
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Function to predict the category of the image
def predict_category(img):
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)  # Get the index of the predicted class
    class_labels = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
                    'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
    return class_labels[class_idx[0]], prediction[0][class_idx[0]]

# Streamlit UI setup
st.set_page_config(page_title="Waste Classification Demo", page_icon=":recycle:", layout="wide")
st.title("Waste Classification Demo with our Trained AI Model")

# Sidebar: Upload Images
st.sidebar.header("Upload Images")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Add a message below the file uploader
st.sidebar.write("Please upload pictures for the following categories:")
categories = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
              'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
st.sidebar.write(", ".join([category.capitalize() for category in categories]))

# Show preview and confirmation for a single uploaded file
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    # Display preview of the uploaded image
    st.image(img, caption="Preview of the uploaded image", use_container_width=True)

    # Add a confirmation button
    if st.button("Confirm Upload"):
        # Predict the category after confirmation
        category, confidence = predict_category(img)

        # Display prediction result
        st.success(f"Predicted Category: {category.capitalize()}")
        st.write(f"Confidence: {confidence:.2f}")
    else:
        st.warning("Please confirm the upload to proceed.")
