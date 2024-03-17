import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(
    page_title="SAFECITY-AI",
    page_icon="👮",
    layout="wide"
)
# Function to create a database and table
def create_database():
    conn = sqlite3.connect('crimedb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS crime (
                    region TEXT,
                    police_station TEXT,
                    total_crime INTEGER,
                    date DATE,
                    crime_rate FLOAT
                )''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(region, police_station, total_crime, date, crime_rate):
    conn = sqlite3.connect('crimedb.db')
    c = conn.cursor()
    c.execute('''INSERT INTO crime VALUES (?, ?, ?, ?, ?)''', (region, police_station, total_crime, date, crime_rate))
    conn.commit()
    conn.close()

# Function to read data from the table
def read_data():
    conn = sqlite3.connect('crimedb.db')
    df = pd.read_sql_query("SELECT * FROM crime", conn)
    conn.close()
    return df

# Function to update data in the table
def update_data(region, police_station, total_crime, date, crime_rate, old_region):
    conn = sqlite3.connect('crimedb.db')
    c = conn.cursor()
    c.execute('''UPDATE crime 
                SET region=?, police_station=?, total_crime=?, date=?, crime_rate=?
                WHERE region=?''', (region, police_station, total_crime, date, crime_rate, old_region))
    conn.commit()
    conn.close()

# Function to delete data from the table
def delete_data(region):
    conn = sqlite3.connect('crimedb.db')
    c = conn.cursor()
    c.execute('''DELETE FROM crime WHERE region=?''', (region,))
    conn.commit()
    conn.close()

# Function to view the complete data table
def view_table():
    df = read_data()
    st.write(df)

# Function to plot interactive graphs using Plotly
def plot_graphs():
    df = read_data()
    fig1 = px.bar(df, x='region', y='total_crime', title='Total Crime by Region')
    fig2 = px.bar(df, x='police_station', y='crime_rate', title='Crime Rate by Police Station')
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

# Main function to run the Streamlit app
def main():
    st.title('Crime Database Management System')
    st.sidebar.title('Menu')

    create_database()

    menu_options = ['View Table', 'Insert Data', 'Update Data', 'Delete Data', 'Plot Graphs']
    choice = st.sidebar.selectbox('Select Option', menu_options)

    if choice == 'View Table':
        view_table()
    elif choice == 'Insert Data':
        st.header('Insert Data')
        region = st.text_input('Region')
        police_station = st.text_input('Police Station')
        total_crime = st.number_input('Total Crime', min_value=0)
        date = st.date_input('Date')
        crime_rate = st.number_input('Crime Rate', min_value=0.0)
        if st.button('Insert'):
            insert_data(region, police_station, total_crime, date, crime_rate)
            st.success('Data inserted successfully!')
    elif choice == 'Update Data':
        st.header('Update Data')
        regions = read_data()['region'].tolist()
        selected_region = st.selectbox('Select Region', regions)
        region = st.text_input('Region', value=selected_region)
        police_station = st.text_input('Police Station')
        total_crime = st.number_input('Total Crime', min_value=0)
        date = st.date_input('Date')
        crime_rate = st.number_input('Crime Rate', min_value=0.0)
        if st.button('Update'):
            update_data(region, police_station, total_crime, date, crime_rate, selected_region)
            st.success('Data updated successfully!')
    elif choice == 'Delete Data':
        st.header('Delete Data')
        regions = read_data()['region'].tolist()
        selected_region = st.selectbox('Select Region', regions)
        if st.button('Delete'):
            delete_data(selected_region)
            st.success('Data deleted successfully!')
    elif choice == 'Plot Graphs':
        st.header('Plot Graphs')
        plot_graphs()

if __name__ == '__main__':
    main()