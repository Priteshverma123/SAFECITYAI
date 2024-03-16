import streamlit as st
import folium
from streamlit_folium import st_folium
import csv
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

for point in data:
    location = point['latitude'],point['longitude']
    folium.Marker(location,tooltip=point['name'],popup="<b>Join Stream<b><br><a target=_blank href='https://youtube.com'>join</a>").add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m,width=8000)