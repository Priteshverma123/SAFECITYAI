import streamlit as st
import folium
from streamlit_folium import st_folium
import csv
from google.cloud import firestore
import json
from transformers import pipeline
import PyPDF2

db = firestore.Client.from_service_account_json("firestore-key.json")
doc_ref = db.collection("StreamData").document("OkMZ5FcclPYmNmToV4kpjhdKZbx1")
doc = doc_ref.get()



datafile="assets/data.csv"

def read_data():
    data=[]
    with open(datafile,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            longitude = row['Longitude']
            latitude = row['Latitude']
            data.append({
                'name': row['Title'],
                'latitude':float(latitude),
                'longitude':float(longitude)
            })
        return data
data = read_data()

st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)

st.title("SAFECITY-AI:LIVE INCIDENT MAP")
m = folium.Map(location=[19.17174137257669, 72.97784619920482],zoom_start=15)
location=float(doc.get("latitude")),float(doc.get("longitude"))

folium.Marker(location,tooltip=doc.get("title"),popup="<b>Join Stream<b><br><a target=_blank href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)
# for point in data:
#     location = point['latitude'],point['longitude']
#     folium.Marker(location,tooltip=point['name'],popup="<b>Join Stream<b><br><a target=_blank href='https://youtube.com'>join</a>").add_to(m)
with open("output.json", 'r') as f:
        data = json.load(f)
for key, value in data.items():
        latitude = value.get('latitude', None)
        longitude = value.get('longitude', None)
        title=value.get('title',None)
        if latitude is not None and longitude is not None:
            folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a target=_blank href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)
# call to render Folium map in Streamlit
st_data = st_folium(m,width=8000)


st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
st.write("Location is ",float(doc.get("latitude")),",",float(doc.get("longitude")))



def pull_and_save_firestore_collection(collection_name, output_file):
    # Get reference to the collection
    collection_ref = db.collection(collection_name)

    # Fetch documents from the collection
    documents = collection_ref.stream()

    # Convert documents to a dictionary
    data = {doc.id: doc.to_dict() for doc in documents}

    # Save data to JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Collection '{collection_name}' saved to '{output_file}'")

# Usage example:
collection_name = 'StreamData'  # Replace 'your_collection_name' with the name of your Firestore collection
output_file = 'output.json'  # Specify the desired output file name
pull_and_save_firestore_collection(collection_name, output_file)







pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Provide the PDF content manually as the context
# Open the PDF file
with open("a1974-02.pdf", "rb") as file:
    # Create a PdfReader object
    reader = PyPDF2.PdfReader(file)
    
    # Extract text from each page
    pdf_text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()

# Define a question to ask
question = st.sidebar.text_input("Enter your question","Hello")

# Use the pipeline to answer the question
result = pipe(question=question, context=pdf_text)

# Display the answer in the sidebar
st.sidebar.header("Answer")
st.sidebar.write(result["answer"])