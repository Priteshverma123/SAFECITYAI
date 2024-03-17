import streamlit as st
import cv2
import tempfile
import numpy as np
from PIL import Image
from transformers import pipeline
import os


st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)

st.title("SAFECITY-AI: LIVE INCIDENT MAP")
st.sidebar.success("Select a page above")
st.sidebar.success("This is a demo")
video_file = st.file_uploader("Upload a video file", type="mp4")
video_path = None
# Display the uploaded video file
if video_file is not None:
     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(video_file.read())
        video_path = temp_file.name


st.subheader("Uploaded Video:")
st.video(video_path)

# Import the pipeline for video classification
from transformers import pipeline

# Instantiate the pipeline for video classification
pipe = pipeline("video-classification", model="shazab/videomae-base-finetuned-ucf_crime2")
result = None
if video_path:
    result = pipe(video_path)

# Remove the temporary file after processing
if video_path:
    os.unlink(video_path)

st.write(result)


# run = st.checkbox('Run')
# stop = st.button('Stop Recording')
# FRAME_WINDOW = st.image([], use_column_width=True)

# # Set the desired width and height for the webcam frame
# width = 640
# height = 480

# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = None

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     # Write the frame to the output video file
#     if out is not None:
#         out.write(frame)
    
#     # Display the frame in the Streamlit app
#     FRAME_WINDOW.image(frame)
    
#     if stop:
#         if out is not None:
#             out.release()  # Release the VideoWriter object after recording stops
#             camera.release()  # Release the camera
            
#             # Pass the recorded mp4 video file to the pipeline for processing
#             result = pipe(video_file)
            
#             # Display the result or take further action based on the inference
#             # For demonstration purposes, print the result to the console
#             print(result)
            
#             out = None
#             break
#         else:
#             break
    
# if run:
#     st.write('Stopped')
