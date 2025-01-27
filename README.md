# Review-Analysis-tool

## **Overview**
The **Review-Analysis-tool** is a powerful tool designed to analyze and summarize product reviews. It leverages advanced Natural Language Processing (NLP) models such as **RoBERTa** for sentiment classification and **BART** for summarization. This application helps businesses and customers gain actionable insights from reviews quickly.

---

## **Features**
- **Sentiment Classification**:
  - Classifies reviews as **Positive** or **Negative** using a fine-tuned RoBERTa model.
- **Review Summarization**:
  - Generates concise summaries for positive and negative reviews separately using the BART model.
- **User-Friendly Interface**:
  - Built with **Streamlit**, the tool offers an interactive and responsive user experience.

---

## **Technologies Used**
1. **Streamlit**: For building the web-based user interface.
2. **Transformers Library**: For utilizing pre-trained models for sentiment analysis and summarization.
3. **Python Libraries**:
   - `pandas` for data manipulation.
   - `nltk` and `transformers` for natural language processing.

---

## **How It Works**
1. **Input**: Users provide multiple product reviews in the text area, each on a new line.
2. **Sentiment Classification**:
   - Each review is classified as positive (`LABEL_1`) or negative (`LABEL_0`) using the fine-tuned RoBERTa model.
3. **Summarization**:
   - Reviews are grouped into positive and negative categories.
   - Summaries are generated for both categories using the BART summarization model.
4. **Output**:
   - Summarized insights for both positive and negative reviews are displayed on the response page.

---
## **Screenshots**
**Home Page**
![review app home page](https://github.com/user-attachments/assets/4e7413b7-2950-41cd-908c-7c12f515d8eb)

**Response Page**
![Review app response](https://github.com/user-attachments/assets/7c38cb0a-ce4a-4f4f-a1d4-e072f97f1521)


## **Notebook for Model Training**
The fine-tuned sentiment analysis model was developed using a comprehensive Jupyter Notebook. Below are the main steps:
	1.	Data Loading:
	•	Load product reviews from a JSON dataset and preprocess the data.
	2.	Sentiment Analysis:
	•	Perform sentiment analysis using VADER and fine-tune a RoBERTa model.
	3.	Review Summarization:
	•	Use the BART model to generate summaries for positive and negative reviews.
	4.	Model Saving:
	•	Save the trained model for deployment.

Refer to the notebook file for a detailed walkthrough.

## **Future Enhancements**
	•	Add support for multilingual reviews.
	•	Provide detailed sentiment scores instead of binary classification.
	•	Enhance UI with advanced visualization features.


**License**
This project is licensed under the MIT License.
