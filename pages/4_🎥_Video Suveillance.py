# import streamlit as st
# import cv2
# import tempfile
# import numpy as np
# from PIL import Image
# from transformers import pipeline
# import os


# st.set_page_config(
#     page_title="SAFECITY-AI",
#     page_icon="👮",
#     layout="wide"
# )
# # Hide the "Made with Streamlit" text
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# st.title("SAFECITY-AI: LIVE INCIDENT MAP")
# st.sidebar.success("Select a page above")
# video_file = st.file_uploader("Upload a video file", type="mp4")
# video_path = None
# # Display the uploaded video file
# if video_file is not None:
#      with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(video_file.read())
#         video_path = temp_file.name


# st.subheader("Uploaded Video:")
# st.video(video_path)

# # Import the pipeline for video classification
# from transformers import pipeline

# # Instantiate the pipeline for video classification
# pipe = pipeline("video-classification", model="shazab/videomae-base-finetuned-ucf_crime2")
# result = None
# if video_path:
#     result = pipe(video_path)

# # Remove the temporary file after processing
# if video_path:
#     os.unlink(video_path)

# st.write(result)


# import streamlit as st
# import cv2
# import tempfile
# import numpy as np
# from PIL import Image
# from transformers import pipeline
# import os

# st.set_page_config(
#     page_title="SAFECITY-AI",
#     page_icon="👮",
#     layout="wide"
# )

# # Hide the "Made with Streamlit" text
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# st.title("SAFECITY-AI: LIVE INCIDENT MAP")
# st.sidebar.success("Select a page above")
# video_file = st.file_uploader("Upload a video file", type="mp4")
# video_path = None

# # Display the uploaded video file
# if video_file is not None:
#      with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(video_file.read())
#         video_path = temp_file.name

# st.subheader("Uploaded Video:")
# st.video(video_path)

# # Instantiate the pipeline for video classification
# pipe = pipeline("video-classification", model="shazab/videomae-base-finetuned-ucf_crime2")
# result = None

# if video_path:
#     result = pipe(video_path)
#     # Filter results with score greater than 90%
#     result = [res for res in result if res['score'] > 0.9]

# # Remove the temporary file after processing
# if video_path:
#     os.unlink(video_path)

# # Display filtered results
# if result:
#     st.write(result)
# else:
#     st.write("No results with score greater than 90%.")

import streamlit as st
import tempfile
import os
from transformers import pipeline

st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)

# Hide the "Made with Streamlit" text
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("SAFECITY-AI: LIVE INCIDENT MAP")
st.sidebar.success("Select a page above")

# Allow users to upload multiple videos
video_files = st.file_uploader("Upload video files", accept_multiple_files=True)

# Instantiate the pipeline for video classification
pipe = pipeline("video-classification", model="shazab/videomae-base-finetuned-ucf_crime2")

# Store results for each video
all_results = []

# Display uploaded videos and perform classification
for video_file in video_files:
    video_path = None
    if video_file is not None:
         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(video_file.read())
            video_path = temp_file.name

    st.subheader("Uploaded Video:")
    st.video(video_path)

    result = None
    if video_path:
        result = pipe(video_path)
        all_results.append(result)

    # Remove the temporary file after processing
    if video_path:
        os.unlink(video_path)

# Display results for each video
for idx, result in enumerate(all_results):
    st.write(f"Results for Video {idx+1}:")
    if result:
        st.write(result)
    else:
        st.write("No results for this video.")

