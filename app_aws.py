import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
from datetime import datetime
import mysql.connector
nltk.download('punkt')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Preprocess text (you can adjust this function as needed)
def preprocess_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    return " ".join(tokens)

# Analyze sentiment using VADER
def analyze_sentiment_vader(text):
    cleaned_text = preprocess_text(text)
    sentiment_scores = analyzer.polarity_scores(cleaned_text)
    return sentiment_scores

# Streamlit app
def streamlit_app():
    tab1, tab2 = st.tabs(["Home", "Sentiment Analysis"])
    with tab1:
        st.markdown('<h1 style="text-align: center; color: red;">GUVI SENTIMENT ANALYSIS</h1>', unsafe_allow_html=True)
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

  
        st.write("### Example of Input and Output")
        st.write("You can enter sentences like:")
        st.markdown("1. **I love this product!** 😍")
        st.markdown("2. **This is the worst experience ever.** 😡")
        st.markdown("3. **It's okay, not great.** 😐")

        name ="User"
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        #if st.button("Login"):
        mycursor.execute(
             "INSERT INTO cust_info (name, login) VALUES (%s, %s)",
                (name, formatted_datetime)
            )
        mydb.commit()
        st.success('Data migrated to RDS-Mysql server!', icon="✅")

    with tab2:
        sentence = st.text_input("Please enter the sentence", "")
        if st.button("Predict Sentiment"):
            sentiment_scores = analyze_sentiment_vader(sentence)
            #st.write(f"Sentiment scores: {sentiment_scores}")

            scores = []
            scores.append(sentiment_scores['neg'])
            scores.append(sentiment_scores['neu'])
            scores.append(sentiment_scores['pos'])
            max_scores = max(scores)
            max_scores_index = scores.index(max_scores)
            if max_scores_index == 0:
                st.subheader(":red[Sentiment of the sentence is] Negative😡")
            elif max_scores_index == 1:
                st.subheader(":orange[Sentiment of the sentence is] Neutral😐")
            else:
                st.subheader(":green[Sentiment of the sentence is] Positive😍")



mydb = mysql.connector.connect(
    host="database-1.c3kemaoiqgvj.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="Sathyabarani",
    port="3306",
    )
mycursor = mydb.cursor(buffered=True)

mycursor.execute("create database if not exists sentimentanalysis")
mycursor.execute("use sentimentanalysis")
mycursor.execute("create table if not exists cust_info (name varchar(255) ,login DATETIME)")


streamlit_app()
