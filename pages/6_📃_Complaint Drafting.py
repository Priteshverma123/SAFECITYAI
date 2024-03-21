import streamlit as st
import easyocr
from PIL import Image
from transformers import pipeline
from PIL import Image


st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)
st.title("SAFECITY-AI")
st.header("COMPLAINT DRAFTING")
st.sidebar.success("Select a page above")
# Hide the "Made with Streamlit" text
hide_streamlit_style = """
            <style>

            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.write("Image file name:", uploaded_image.name)

reader = easyocr.Reader(['en'])  # You can specify additional languages if needed

image = Image.open(uploaded_image)
extracted_text = reader.readtext(image)
cleaned_text = '\n'.join([text[1] for text in extracted_text])
st.write("Extracted Text:")
st.write(cleaned_text)


# Load the question answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad")

# Input text
context =  cleaned_text

# Question
question = st.text_input("Ask your question:")

# Run the question answering pipeline
result = qa_pipeline(question=question, context=context)

# Output the answer
st.write(f"Question: {question}")
st.write(f"Answer: {result['answer']}")


