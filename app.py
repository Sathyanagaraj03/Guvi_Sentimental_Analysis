import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, DateTime, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd


# Set up MySQL connection
engine = create_engine("mysql+mysqlconnector://root:""@localhost/sentimental_analysis")

# Create a metadata object to manage the table schema
metadata = MetaData()

# Define the table schema for timestamps
timestamps_table = Table(
    'timestamps', metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp_column', DateTime)
)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Function to insert the current date and time into the database
def insert_timestamp_to_db():
    # Get the current date and time
    current_datetime = datetime.now()

    # Create a new session
    session = Session()

    # Insert the timestamp into the table
    insert_query = timestamps_table.insert().values(timestamp_column=current_datetime)

    # Execute the query
    session.execute(insert_query)
    
    # Commit the transaction
    session.commit()

    # Close the session
    session.close()

    return current_datetime

# Save the current date and time when the Streamlit app is opened
current_datetime = insert_timestamp_to_db()

# Load the saved sentiment analysis model and TF-IDF vectorizer
with open('decision_tree_sentiment_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Function to clean input text for sentiment analysis
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Streamlit App Title
st.title("Sentiment Analysis with Decision Tree Model")

# Create tabs for project explanation and sentiment prediction
tab1, tab2 = st.tabs(["Project Explanation", "Sentiment Prediction"])
# Project explanation tab
with tab1:
    st.header("Project Explanation")
    
    st.write("""
        This project implements a sentiment analysis model using a **Decision Tree classifier**. 
        The model analyzes text input and classifies it as **Negative**, **Neutral**, or **Positive**. 
        The application utilizes a **TF-IDF vectorizer** to transform the input text into numerical 
        features that can be processed by the model.
    """)

    # Add an image (make sure to have an appropriate image path)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe31SWTdSuedDA0St9kcxrv995vW0WWd8Umg&s", caption="Sentiment Analysis Workflow", use_column_width=True)

    st.markdown("<h3 style='color:blue;'>How It Works:</h3>", unsafe_allow_html=True)
    
    st.write("""
        1. **Input**: Users can input any text they wish to analyze. 📝
        2. **Preprocessing**: The input text is cleaned and transformed using the **TF-IDF vectorizer**. 🔄
        3. **Prediction**: The model predicts the sentiment of the text based on the processed input. 🔍
        4. **Output**: Users can choose how they want the sentiment to be displayed (simple text, with emojis, etc.). 🎨
    """)

    # Adding a colored box to emphasize a point
    st.markdown("""
        <div style='background-color:lightyellow; padding:10px; border-radius:5px'>
            <strong>Note:</strong> This application is built using Streamlit, allowing for interactive web applications.
        </div>
    """, unsafe_allow_html=True)

    st.write("### Example of Input and Output")
    st.write("You can enter sentences like:")
    st.markdown("1. **I love this product!** 😍")
    st.markdown("2. **This is the worst experience ever.** 😡")
    st.markdown("3. **It's okay, not great.** 😐")

# Sentiment prediction tab
with tab2:
    st.header("Enter Text for Sentiment Analysis")
    # Display the current date and time (saved to the database)
    st.write("Current Date and Time (Logged):", current_datetime)

    # User input for sentiment analysis
    user_input = st.text_area("Enter text for sentiment analysis:")

    # If the user enters text, process it
    if user_input:
        # Clean and preprocess the user input
        cleaned_input = clean_text(user_input)
        input_tfidf = tfidf.transform([cleaned_input])

        # Predict sentiment using the Decision Tree model
        prediction = model.predict(input_tfidf)[0]

        if prediction == 0:
                sentiment = "😠 Negative"
        elif prediction == 1:
                sentiment = "😐 Neutral"
        else:
                sentiment = "😊 Positive"
        st.write(f"**Predicted Sentiment:** {sentiment}")

