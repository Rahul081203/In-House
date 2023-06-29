import cv2
import tensorflow as tf
import numpy as np
from keras.models import load_model
# import os

# Load the trained model
model = load_model(r'c:\users\rahul\documents\ntcc_4th_sem\webpage\sign_classifier_model.h5')

# Mapping for class labels
mapping = {i: str(i+1) for i in range(9)}
for i, letter in enumerate(range(9, 35)):
    mapping.update({letter: chr(ord('A') + i)})

# Define a function to preprocess the frame before making predictions
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges_3ch = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    preprocessed_frame = cv2.resize(edges_3ch, (256, 256))
    # preprocessed_frame = preprocessed_frame / 255.0  # Normalize the frame
    return preprocessed_frame


def classify_sign(frame):
    # Preprocess the frame
    preprocessed_frame = preprocess_frame(frame)

    # Resize the original frame to match the dimensions of the preprocessed image
    resized_frame = cv2.resize(frame, (256,256))

    # Create a side-by-side comparison of the resized frame and preprocessed image
    # combined_frame = np.hstack((resized_frame, preprocessed_frame))

    # Expand dimensions to match the model's input shape
    input_data = np.expand_dims(preprocessed_frame, axis=0)

    # Make a prediction using the model
    predictions = model.predict(input_data)

    # Get the predicted class
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Get the corresponding label from the mapping
    predicted_label = mapping[predicted_class]

    # Display the predicted label on the frame
    cv2.putText(resized_frame, 'Predicted: {}'.format(predicted_label), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

    return resized_frame


def process_webcam_feed():
    # Create an instance of cv2.VideoCapture
    cap = cv2.VideoCapture(1)

    while True:
        # Read the frame from the video capture
        ret, frame = cap.read()

        if not ret:
            # Break the loop if there is an issue reading the frame
            break
        combined_frame = classify_sign(frame)

        # Display the combined frame in a window
        cv2.imshow('Video Capture (Original vs Preprocessed)', combined_frame)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()
