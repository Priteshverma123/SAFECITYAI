import streamlit as st
import folium
from streamlit_folium import st_folium
import csv
from google.cloud import firestore
import json
from io import BytesIO
import base64
import random
import math
@st.cache_data
def generate_random_coordinates(center, radius, num_points):
    random_coords = []
    for _ in range(num_points):
        # Generate random offsets within the radius
        dx = random.uniform(-50, 50) * (radius / 1)  # Adjust the scale as needed
        dy = random.uniform(-50, 50) * (radius / 1)  # Adjust the scale as needed
        
        # Calculate new coordinates with offset
        new_lat = center[0] + (180 / (2 * 6378137)) * (dy / (10 ** 5))
        new_lon = center[1] + (180 / (2 * 6378137 * math.cos(math.pi * center[0] / 180))) * (dx / (10 ** 5))
        
        random_coords.append({'latitude': new_lat, 'longitude': new_lon, 'title': f'Patrol Car ID. {len(random_coords) + 1}'})

    return random_coords


icon_path = "assets\police.png"
icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))


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
st.sidebar.success("Select a page above")
st.title("SAFECITY-AI:LIVE INCIDENT MAP")
# Set the center location
center_location = [19.1813801, 72.8475999]  # London coordinates
# Set the radius in degrees (adjust as needed)
radius_degrees = 1000000
num_markers = 16


random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
# random_coordinates = [
#     {'latitude': 19.050413800011277, 'longitude': 72.87844360004112, 'title': 'Marker 1'},
#     {'latitude': 19.050413800037386, 'longitude': 72.87844359998012, 'title': 'Marker 2'},
#     {'latitude': 19.05041380002946, 'longitude': 72.87844360000626, 'title': 'Marker 3'},]

m = folium.Map(location=[19.17174137257669, 72.97784619920482],zoom_start=15)


location=float(doc.get("latitude")),float(doc.get("longitude"))








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
            folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)
# call to render Folium map in Streamlit
for coord in random_coordinates:
    latitude = coord['latitude']
    longitude = coord['longitude']
    title = coord['title']
    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
    folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)




st_data = st_folium(m,width=8000)


folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


st.write("Location is ",float(doc.get("latitude")),",",float(doc.get("longitude")))
st.write(data)







# Generate random coordinates around the center location


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