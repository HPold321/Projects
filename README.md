# Streamlit Chatbot with Hugging Face Models

This project is a chatbot created from scratch using a Streamlit UI and Hugging Face models in Python. The chatbot utilizes a text-to-text pipeline with a pre-trained model from Hugging Face to generate coherent answers based on provided questions and contexts.

## Project Structure

- `app.py`: Contains the Streamlit UI code for the chatbot.
- `data.py`: Handles data loading and preprocessing.
- `war.csv`: CSV file containing questions and their corresponding contexts.
- `ww2.csv`: CSV file where the generated answers are saved.

## Features

- **Text-to-Text Pipeline**: Utilizes the `bart-large-cnn` model from Hugging Face for generating answers.
- **Question-Answering**: Generates a minimum one-line coherent answer based on the provided question and context.
- **Similarity Computation**: Computes similarity between user input and each question in the dataset, retrieves the highest similarity question and its corresponding answer and context.
- **Polite Responses**: Provides a polite answer if the chatbot does not have sufficient information in its database.

## Requirements

- Python 3.6+
- Streamlit
- Transformers (Hugging Face)
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamlit-chatbot.git
   cd streamlit-chatbot
   ```
2. Download the required packages from pip:
   ```bash
   pip3 install spacy
   pip3 install transformer
   pip3 install streamlit
   ```
## Usage:
1. Download the files app.py, data.py, war.csv. You can also use any other csv file following the same structure.
2. Run '$ streamlit run app.py' on your terminal.

## Contributing:
Used this model from Hugging face.. 'facebook/bart-large-cnn'. 
@article{DBLP:journals/corr/abs-1910-13461,
  author    = {Mike Lewis and
               Yinhan Liu and
               Naman Goyal and
               Marjan Ghazvininejad and
               Abdelrahman Mohamed and
               Omer Levy and
               Veselin Stoyanov and
               Luke Zettlemoyer},
  title     = {{BART:} Denoising Sequence-to-Sequence Pre-training for Natural Language
               Generation, Translation, and Comprehension},
  journal   = {CoRR},
  volume    = {abs/1910.13461},
  year      = {2019},
  url       = {http://arxiv.org/abs/1910.13461},
  eprinttype = {arXiv},
  eprint    = {1910.13461},
  timestamp = {Thu, 31 Oct 2019 14:02:26 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-13461.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

