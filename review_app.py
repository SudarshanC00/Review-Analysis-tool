import streamlit as st
from transformers import pipeline
import pandas as pd



# Load models
@st.cache_resource
def load_models():
    classifier = pipeline("text-classification", model="/Users/sudarshanc/Projects/Review_analysis/sentiment_model", tokenizer="/Users/sudarshanc/Projects/Review_analysis/sentiment_model")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return classifier, summarizer

classifier, summarizer = load_models()

# Streamlit app title
st.title("Review Analysis and Summary Generator")

# Input from the user
st.header("Enter Product Reviews")
user_reviews = st.text_area(
    "Provide multiple reviews about a product, each on a new line.",
    placeholder="Example:\nThe product is amazing!\nBattery life is disappointing.\nThe sound quality is superb."
)

def summarize_reviews(reviews, summarizer, max_length=50, min_length=20):
    combined_text = " ".join(reviews)
    
    # Generate the summary
    summary = summarizer(
        combined_text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return summary[0]['summary_text']

# Analyze reviews if input is provided
if user_reviews:
    reviews = user_reviews.split("\n")
    reviews = [review.strip() for review in reviews if review.strip()]
    
    # Classify reviews
    classifications = classifier(reviews)

    label_list = [pred['label'] for pred in classifications]
    df_pred = pd.DataFrame({'review': reviews, 'label': label_list})
    pred_pos = pd.DataFrame(df_pred[df_pred['label'] == 'LABEL_1'])
    pred_neg = pd.DataFrame(df_pred[df_pred['label'] == 'LABEL_0'])

    
    # Generate summaries
    st.subheader("Generated Summaries")
    
    # Summarize positive reviews
    positive_summary = summarize_reviews(pred_pos['review'].tolist(), summarizer)

    # Summarize negative reviews
    negative_summary = summarize_reviews(pred_neg['review'].tolist(), summarizer)

    # Display the summaries
    st.write("Positive Reviews Summary:")
    st.write(positive_summary)

    st.write("\nNegative Reviews Summary:")
    st.write(negative_summary)
    