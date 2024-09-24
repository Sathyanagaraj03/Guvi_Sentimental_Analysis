# Sentiment Analysis Streamlit Application

![Sentiment Analysis](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe31SWTdSuedDA0St9kcxrv995vW0WWd8Umg&s)

This project implements a sentiment analysis model using a Decision Tree classifier. The model analyzes text input and classifies it as **Negative**, **Neutral**, or **Positive**. The application utilizes a TF-IDF vectorizer to transform the input text into numerical features that can be processed by the model.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Methodology](#methodology)
4. [Modeling](#modeling)
5. [Evaluation](#evaluation)
6. [Results](#results)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

The sentiment analysis model helps in understanding public opinion by classifying sentiments expressed in text data. It can be applied to various domains, including social media analysis, customer feedback, and market research. This application uses historical sentiment data to train the model and provide real-time sentiment predictions.

---

## Installation

### Requirements

To run the project, you will need the following installed:

- Python 3.8+
- Streamlit 0.86+
- Scikit-learn 1.0+
- Pandas 1.3+
- NumPy 1.21+

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Sathyanagaraj03/sentiment-analysis-streamlit.git
    cd sentiment-analysis-streamlit
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

---

## Methodology

1. **Data Collection**: Gather text data for sentiment analysis.
2. **Data Preprocessing**:
   - Clean the text data (remove noise, punctuation, etc.)
   - Transform text data using TF-IDF vectorization.
3. **Model Training**:
   - Use a Decision Tree classifier to predict sentiment labels based on the processed input.
4. **Deployment**:
   - Create a Streamlit application for user input and display predictions.

---

## Modeling

We utilize a Decision Tree classifier for sentiment prediction, which provides an interpretable model for classifying sentiments based on text features.

---

## Evaluation

We evaluate model performance using various metrics, including:

- **Accuracy**: The ratio of correctly predicted instances to the total instances.
- **Precision**: The ratio of true positives to the sum of true and false positives.
- **Recall**: The ratio of true positives to the sum of true positives and false negatives.
- **F1 Score**: The harmonic mean of precision and recall.

Visualizations of the prediction results are provided to assess model performance.

---

## Results

- **Best Model**: The Decision Tree model achieved satisfactory performance on sentiment classification.
- **Key Features**: The TF-IDF vectorizer highlights important words that contribute to sentiment classification.

---
## Demo

You can view a live demo of the application at the following link:

[Live Demo](https://sentimentalanalysis01.streamlit.app/)

---
## Future Work

- Explore advanced models like Support Vector Machines or neural networks for improved accuracy.
- Integrate real-time data collection and analysis from social media platforms.
- Enhance the application’s user interface for better user experience.
- Expand the sentiment categories (e.g., adding more nuanced sentiments).

---

## Contributing

We welcome contributions! If you want to contribute, please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
