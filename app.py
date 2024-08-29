import streamlit as st
import cv2
import numpy as np

# Function to initialize camera based on user selection
def init_camera(source):
    if source == "Local Camera (Webcam)":
        return cv2.VideoCapture(0)
    elif source == "External Camera (IP Camera)":
        camera_url = st.text_input("Enter IP Camera URL:", value="")
        if camera_url:
            return cv2.VideoCapture(camera_url)
        else:
            st.error("Please enter a valid IP camera URL.")
            return None
    else:
        st.error("Invalid source selected.")
        return None

# Function to capture frames from the camera
def get_frame(camera):
    success, frame = camera.read()
    if not success:
        return None
    # Convert the frame to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Streamlit UI
st.title("Video Streaming with Streamlit")

# Dropdown for selecting camera source
camera_source = st.selectbox("Select Camera Source", ["Local Camera (Webcam)", "External Camera (IP Camera)"])

# Initialize camera based on user selection
camera = init_camera(camera_source)

if camera:
    # Create a placeholder for the video
    stframe = st.empty()
    
    # Stream video
    while True:
        frame = get_frame(camera)
        if frame is None:
            st.error("Failed to capture video.")
            break
        # Display the video frame in the Streamlit app
        stframe.image(frame, channels="RGB", use_column_width=True)
        st.sleep(0.1)  # Add a small delay to prevent high CPU usage

    # Release the camera when done
    camera.release()
else:
    st.error("Camera could not be initialized.")
