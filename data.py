#! pip3 install transformers
import pandas as pd
from transformers import pipeline
import csv

# Load the question answering pipeline
qa_pipeline = pipeline("text2text-generation", model="facebook/bart-large-cnn")

# Read the CSV file into a DataFrame
df = pd.read_csv("war.csv", delimiter=";", header=None, names=["Question", "Context"])

# Open a new CSV file to save question, answer, and context
with open("ww2.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=";")  # specify the delimiter here
    csv_writer.writerow(["Question", "Answer", "Context"])  # Write header

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # Check if question or context is NaN
        if pd.isna(row["Question"]) or pd.isna(row["Context"]):
            continue  # Skip if NaN
        
        question = str(row["Question"]).strip()
        context = str(row["Context"]).strip()

        # Truncate the context to a reasonable length
        context = context[:512]  # Adjust the length as needed

        # Construct prompt for generating coherent answers
        prompt = f"Question: {question}\nContext: {context}\n"

        # Generate answer using the question answering pipeline
        answer = qa_pipeline(prompt, max_length=100, num_return_sequences=1)[0]['generated_text'].strip()

        # Write the question, answer, and context to the new CSV file
        csv_writer.writerow([question, answer, context])
