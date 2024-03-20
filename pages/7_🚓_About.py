import streamlit as st
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT , title TEXT, article TEXT, postdate DATE)')

def add_data(author, title, article, postdate):
    c.execute('INSERT INTO blogtable(author, title, article, postdate) VALUES (?, ?, ?, ?)', (author, title, article, postdate))
    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data= c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT author, title, article, postdate FROM blogtable WHERE title=?', (title,))
    data = c.fetchall()
    return data

#layout
title_temp= """
    <div style="background-color:#464e5f;padding:10px;margin:10px; border-radius:15px">
    <h4 style="color:white;text-align:center;">{}</h4>
    <img src="https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png" alt="Avatar" style="vertical-align: middle;float: left;width: 50px;height: 50px;">
    <h6>Author:{}</h6>
    </br>
    </br>
    <p style="text-align: justify">{}</p>
    </div>
    """
article_temp= """
    <div style="background-color:#464e5f;padding:10px;margin:10px; border-radius: 15px">
    <h4 style="color:white;text-align:center;">{}</h4>
    <img src="https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png" alt="Avatar" style="vertical-align: middle;float: left;width: 50px;height: 50px;">
    <h6>Author:{}</h6>
    <h6>Post Date:{}</h6>
    </br>
    </br>
    <p style="text-align: justify">{}</p>
    </div>
    """
head_message_temp= """
    <div style="background-color:#464e5f;padding:10px;margin:10px; border-radius:15px">
    <h4 style="color:white;text-align:center;">{}</h4>
    <img src="https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png" alt="Avatar" style="vertical-align: middle;float: left;width: 50px;height: 50px;">
    <h6>Author:{}</h6>
    </div>
    """
full_message_temp= """
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius: 10px;margin:10px">
    <p style="text-align: justify; color: black;padding": 10px">{}</p>
    </div>
    """


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
st.sidebar.success("Select a page above")

def main():
    st.title("SAFECITY-AI: ARTICLES ")
    menu = ["Home", "View Articles", "Add Articles"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        result = view_all_notes()
        for i in result:
            b_author=i[0]
            b_title= i[1]
            b_article= i[2]
            b_postdate= i[3]
            st.markdown(title_temp.format(b_title,b_author,b_article,b_postdate),unsafe_allow_html=True)
    elif choice == "View Articles":
        st.subheader("View Articles")
        all_titles= [i[0] for i in view_all_titles()]
        postlist= st.sidebar.selectbox("View Posts", all_titles)
        post_result= get_blog_by_title(postlist)
        for i in post_result:
            b_author=i[0]
            b_title= i[1]
            b_article= i[2]
            b_postdate= i[3]
            st.markdown(head_message_temp.format(b_title,b_author,),unsafe_allow_html=True)
            st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)
        # Add code to view articles here
    elif choice == "Add Articles":
        st.subheader("Add Articles")
        create_table()
        blog_author = st.text_input("Enter Author Name:", max_chars=50)
        blog_title = st.text_input("Enter Article Title")
        blog_article = st.text_area("Post Article Here", height=200)
        blog_post_date = st.date_input("Date")
        if st.button("Add"):
            add_data(blog_author, blog_title, blog_article, blog_post_date)
            st.success("Post '{}' saved".format(blog_title))

if __name__ == '__main__':
    main()