import streamlit as st
import folium
from streamlit_folium import st_folium
from google.cloud import firestore
import random
import json
import math
@st.cache_data
def generate_random_coordinates(center, radius, num_points):
    random_coords = []
    for _ in range(num_points):
        # Generate random offsets within the radius
        dx = random.uniform(-50000, 50000) * (radius / 1)  # Adjust the scale as needed
        dy = random.uniform(-50000, 50000) * (radius / 1)  # Adjust the scale as needed
        
        # Calculate new coordinates with offset
        new_lat = center[0] + (180 / (2 * 6378137)) * (dy / (10 ** 5))
        new_lon = center[1] + (180 / (2 * 6378137 * math.cos(math.pi * center[0] / 180))) * (dx / (10 ** 5))
        
        random_coords.append({'latitude': new_lat, 'longitude': new_lon, 'title': f'Patrol Car ID. {len(random_coords) + 1}'})

    return random_coords

st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)
st.sidebar.success("Select a page above")
# Hide the "Made with Streamlit" text
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Create a sidebar menu with a dropdown for city selection
selected_city = st.sidebar.selectbox('Select a city:', ['Vijaywada', 'Vishakpatnam', 'Guntur', 'Eluru', 'Amravati', 'Rajamahendravaram'])

# Display the content of the selected city
if selected_city == 'Vijaywada':
    st.header("VIJAYWADA")
    police_stations = [
     {'latitude': 16.50817365159962,  'longitude': 80.64573691637011, 'title': '/Vijayawada Police Station'},
     {'latitude': 16.497755245359485, 'longitude': 80.69054005982692, 'title': 'Penamaluru Police Station'},
     {'latitude': 16.533737636126276, 'longitude': 80.64954481859043, 'title': 'Gunadala Police Station'},
     {'latitude': 16.554216925462832, 'longitude': 80.65185440964599, 'title': 'Nunna Police Station'},
     {'latitude': 16.523296066677524, 'longitude': 80.62713078952531, 'title': 'Governorpeta Police Station'},
     {'latitude': 16.52818,           'longitude': 80.65700,          'title': 'Machavaram Police Station'}  
     

    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))

    # Set the center location
    center_location = [16.50817365159962, 80.64573691637011]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[16.50817365159962, 80.64573691637011],zoom_start=15)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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





elif selected_city == 'Vishakpatnam':
    st.header("VISHAKAPATNAM")
    police_stations = [
     {'latitude': 17.74973014010475,  'longitude': 83.21975317179863, 'title': 'Gopalapatnam Police Station'},
     {'latitude': 16.614334401505293, 'longitude': 80.5372372562447,  'title': 'Kondapalli Ward 2 secretariat'},
     {'latitude': 16.59725818010486,  'longitude': 80.52308098606647, 'title': 'Ibrahimpatnam Police Station'},
     {'latitude': 17.793496893493373, 'longitude': 83.35176565249141, 'title': 'Cyber Crime Police Station'},
     {'latitude': 17.013949250870326,  'longitude':81.76951349003437, 'title': '3 Town Police Station'},
     {'latitude': 17.007383201196564,  'longitude':81.7722600721504, 'title': 'ONE TOWN POLICE STATION'},
     {'latitude': 16.997862020359143,  'longitude': 81.77603662255996, 'title': 'Two Town Police Station'}


    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))

    # Set the center location
    center_location = [17.74973014010475, 83.21975317179863]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[17.74973014010475, 83.21975317179863],zoom_start=15)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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






elif selected_city == 'Guntur':
    st.header("GUNTUR")
    police_stations = [
     {'latitude': 16.314732507263027, 'longitude': 80.45106638916272, 'title': 'Kothapet Police Station'},
     {'latitude': 16.337967766433874, 'longitude': 80.48031700330911, 'title': 'Pedakakani Police Station'},
     {'latitude': 16.29491153504116,  'longitude': 80.446967920815,   'title': 'Lalapet Police Station'},
     {'latitude': 16.295703229995578, 'longitude': 80.45232478799053, 'title': 'Old Guntur Police Station'},
     {'latitude': 16.311012065273566, 'longitude': 80.42200275387995, 'title': 'Pattabhipuram Police Station'},   
     {'latitude': 16.44660955502937,  'longitude': 80.59317823709394, 'title': 'AP POLICE 9'}


    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))


    # Set the center location
    center_location = [16.314732507263027, 80.45106638916272]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[16.314732507263027, 80.45106638916272],zoom_start=15)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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





elif selected_city == 'Eluru':
    st.header("ELURU")
    police_stations = [
     {'latitude': 16.722614013895583, 'longitude': 81.12086194928708, 'title': 'Sub Divisional Police Officaru Vari Karyalayamu'},
     {'latitude': 16.712723796848618, 'longitude': 81.08123305304612, 'title': 'Office of the D.I.G Of Police'},
     {'latitude': 16.7145323001105,   'longitude': 81.09359267256826, 'title': '2 Town Police Station'},
     {'latitude': 16.71732722597967,  'longitude': 81.10560896932594, 'title': 'Police Sub Control'},
     {'latitude': 16.71243150835837,  'longitude': 81.08633383570537, 'title': '3 Town Police Station'},    
     {'latitude': 17.73780501784402,  'longitude': 83.33044163870301, 'title': '3 Town Police Station'}
    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))


    # Set the center location
    center_location = [16.712723796848618, 81.08123305304612]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[16.712723796848618, 81.08123305304612],zoom_start=15)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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




elif selected_city == 'Amravati':
    st.header("AMRAVATI")
    police_stations = [
     {'latitude': 16.520980582623306, 'longitude': 80.52472226380587, 'title': 'Amaravati Police OutPost'},
     {'latitude': 16.515219874767844, 'longitude': 80.51933498644594, 'title': 'Amaravati Traffic Police Station'},   
     {'latitude': 17.73081893245643,  'longitude': 83.30261611814677, 'title': '2 Town Police Station'},
     {'latitude': 17.72615902670698,  'longitude': 83.29571625391469, 'title': 'Police Control Room'},
     {'latitude': 16.572995598891445, 'longitude': 80.54143047675305, 'title': 'Guntupalli Sub Station'},
     {'latitude': 17.74973014010475,  'longitude': 83.21975317179863, 'title': 'Gopalapatnam Police Station'},
     {'latitude': 16.614334401505293, 'longitude': 80.5372372562447,  'title': 'Kondapalli Ward 2 secretariat'},
     {'latitude': 16.59725818010486,  'longitude': 80.52308098606647, 'title': 'Ibrahimpatnam Police Station'}

    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))


    # Set the center location
    center_location = [16.520980582623306, 80.52472226380587]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[16.614334401505293, 80.5372372562447],zoom_start=13)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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





elif selected_city == 'Rajamahendravaram':
    st.header("RAJAMAHENDRAVARAM")
    police_stations = [
     {'latitude': 17.010801771725358, 'longitude': 81.77750124537803, 'title': 'Rajahmundry City Traffic Police Station'},
     {'latitude': 17.02812457060168,  'longitude': 81.80439238142831, 'title': 'Office Of Superintendent Of Police'},
     {'latitude': 17.01327366887392,  'longitude': 81.76776322695733, 'title': 'Office Of Deputy Superintendent Of Police -Crimes'},
     {'latitude': 17.02255918809501,  'longitude': 81.80493775866381, 'title': 'DSP Office, East Zone,Rajahmundry'},
     {'latitude': 17.02040999880307,  'longitude': 81.80824664077987, 'title': 'Rajahmundry Rural Police Circle Office'},
     {'latitude': 17.05582714187831,  'longitude': 81.79685241801535, 'title': 'Konthamuru Police Station'}


    # Add more data entries as needed
    ]

    icon_path = "assets\police.png"
    icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))


    # Set the center location
    center_location = [17.01327366887392, 81.76776322695733]  # andhra pradesh
    # # Set the radius in degrees (adjust as needed)
    radius_degrees = 10000
    num_markers = 15
    db = firestore.Client.from_service_account_json("firestore-key.json")
    doc_ref = db.collection("StreamData").document("pw9VDwUUQseUSKADAh9UHCNmN152")
    doc = doc_ref.get()
    random_coordinates = generate_random_coordinates(center_location, radius_degrees, num_markers)
    m = folium.Map(location=[17.01327366887392, 81.76776322695733],zoom_start=15)
    with open("output.json", 'r') as f:
        data = json.load(f)
    for key, value in data.items():
            latitude = value.get('latitude', None)
            longitude = value.get('longitude', None)
            title=value.get('title',None)
            if latitude is not None and longitude is not None:
                folium.Marker([latitude, longitude],tooltip=title,popup="<b>Join Stream<b><br><a href='https://sharib-livestream-1523.app.100ms.live/streaming/meeting/ypk-nxpz-zru'>join</a>").add_to(m)

    for coord in random_coordinates:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\police.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)

    for coord in police_stations:
        latitude = coord['latitude']
        longitude = coord['longitude']
        title = coord['title']
        icon_path = "assets\Police_Station.png"
        icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(45,45))
        folium.Marker(location=[latitude, longitude],tooltip=title,icon=icon).add_to(m)


    st_data = st_folium(m,width=8000)


    folium.Marker(location=[19.150413800011277, 72.87844360004112]).add_to(m)


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

