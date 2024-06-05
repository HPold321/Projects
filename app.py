import streamlit as st
import pandas as pd
import spacy

# Load the spaCy English model with word vectors
nlp = spacy.load("en_core_web_md")

# Load the dataset
twist_data = pd.read_csv("ww2.csv", delimiter=";")

def generate_response(user_input):
    # Compute similarity between the user input and each question in the dataset
    similarities = []
    for index, row in twist_data.iterrows():
        question = row["Question"]
        doc = nlp(question)
        similarity = doc.similarity(nlp(user_input))
        similarities.append((index, question, similarity))

    # Sort the similarities in descending order
    similarities.sort(key=lambda x: x[2], reverse=True)

    # Retrieve the highest similarity question and its corresponding answer and context
    top_match_index, top_match_question, top_similarity = similarities[0]
    top_match_answer = twist_data.loc[top_match_index, "Answer"]
    top_match_context = twist_data.loc[top_match_index, "Context"]

    # Check if the similarity is above a threshold (you can adjust this threshold as needed)
    if top_similarity > 0.6:  # Adjust the threshold as needed
        return f"Question you gave: {user_input}\n\nAnswer: {top_match_answer}"
    else:
        return "Sorry, I couldn't find an answer to that question."

def main():
    st.title("World War 2 Trivia Chatbot")
    st.text("You can ask this chatbot any questions about WW2 !")
    
    user_input = st.text_input("You:", "")
    if st.button("Send"):
        # Process user input and generate chatbot response
        bot_response = generate_response(user_input)
        st.text_area("Chatbot:", value=bot_response, height=200)

if __name__ == "__main__":
    main()
