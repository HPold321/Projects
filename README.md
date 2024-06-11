# Prompting In Mistral

This repository contains a simple script to load and use the Mistral-7B-v0.1-GGUF model with the `ctransformers` library.

## Requirements

- Python 3.6+
- GPU (optional for acceleration)
- ctransformers
- A hugging face account

## Installation

1. Clone the repository:

2. Install the required dependencies as given in the requirements.

## Parameters
gpu_layers: Number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system. 

model_file: Path to the model file.

model_type: Type of the model.

### Example
To run the script, execute:

```bash
python your_script_name.py
```
Replace your_script_name.py with the name of your script file containing the provided code.

## Usage

- This script demonstrates how to load the Mistral-7B-v0.1-GGUF model and generate text using the `ctransformers` library.
- You might need to load hugging face CLI to give authentication, tokens, etc. 
- You would need to add the model to authorized in your hugging face account and use your privately generated 'finegrain' token. Give it permission to author programs with the free model before you can run th main.py file. 

I am using this model for Content genneration and basically just observing how different prompting technques give different outputs and which one can be used. 

## OBSERVATIONS...
**Prompt-Output Consistency:**

- The outputs generally address the prompts directly, but sometimes they deviate or fail to meet specific requirements (e.g., the need for a JSON format in entry 7 is not met).
- I realize that punctuation plays a big role in this. Entry 5 and 6 prompts have the same content with different punctuations. And the results vary. One is turned into a book review and goes on to describe its hypothetical author. While the other returns a genuine story with the main character Jasper.

**Story Generation:**

- Entries 2, 4, and 6 involve generating fairy tales or stories. The model creates narratives with coherent structure and follows the given instructions reasonably well.
- For example, in entry 2, the generated fairy tale includes a main character with a challenge, a secondary character, and a resolution, as required by the prompt.

**Information Retrieval and Summarization:**

- Entries like 1, 3, and 11 show the model's ability to retrieve and summarize information. The output in entry 1 provides a structured explanation about buying vegetables directly from local farmers.
- Entry 12 demonstrates the model's summarization capability, condensing text into a shorter form effectively.

**Fill-in-the-Blanks Tasks:**

- Entry 10 involves a fill-in-the-blanks exercise about Albert Einstein. I expected the model to return maybe a phrase/ word to fill in the stoy. Instead, it returned more fill in the blank questions.
- The responses seem accurate and contextually appropriate, demonstrating the model's ability to complete sentences based on partial input.

**Errors and Format Issues:**

- Entry 7 shows a clear format issue where the output does not comply with the JSON format request.
- Entry 8, though providing guidelines for generating a story, does not output the story itself within the visible data.

**Miscellaneous Outputs:**

- Some entries contain detailed information that goes beyond the immediate prompt (e.g., entry 3 includes a description of goldfinch stories and their relevance).

## License
This project is licensed under the MIT License - see the LICENSE file for details.

```csharp
This `README.md` provides an overview of the project, installation instructions, usage examples, and license information. You can customize it further based on your specific project details.
```
## Contributors/ Citations
"TheBloke. (2022). Mistral-7B-v0.1-GGUF. Hugging Face Model Hub. Retrieved from https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF"
