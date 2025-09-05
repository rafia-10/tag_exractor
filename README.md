# Tag Extraction Project

A versatile Tag Extraction tool that combines Gazetteer-based, spaCy NLP, and Groq LLM extraction methods to identify relevant tags from text. Designed for ease of use and high accuracy, this project allows users to extract structured information from unstructured text.

## Features

Gazetteer Extraction: Matches input text against a curated list of known entities for precise tag recognition.

spaCy Extraction: Leverages Named Entity Recognition (NER) for linguistic-based tag extraction.

Groq LLM Extraction: Uses the Groq Large Language Model to extract semantic tags from input text.

Prioritized Tag Extraction: Combines all three methods with configurable priorities to improve accuracy.

Interactive User Input: Enter any text and receive structured tags in real-time.

## Getting Started
### 1. Clone the Repository

     git clone https://github.com/yourusername/tag-extraction.git
     cd tag-extraction
     
### 2. Create a Conda Environment

    conda create -n tag-extractor python=3.11 -y
    conda activate tag-extractor

### 3. Install dependencies
    pip install -r requirements.txt
⚠️ Note: Make sure to have your Groq API key set in the environment:

## Usage

Run the combined tag extractor:

        python3 combined_extractor.py

Enter your text when prompted.

The script will return tags extracted from Gazetteer, spaCy, and Groq LLM.

Tags are combined based on predefined priorities.

## Project structure

tag_extraction/
│
├── combined_extractor.py     # Main script combining all extraction methods
├── gazetteer_extractor.py    # Extract tags using a curated gazetteer
├── spacy_extractor.py        # Extract tags using spaCy NLP
├── llm_extractor.py          # Extract tags using Groq LLM
├── data/
│   └── gazetteer.json        # List of known entities for Gazetteer extraction
├── requirements.txt          # Python dependencies
└── README.md   


## Example

### Input Text:
      We trained a GAN using PyTorch on CIFAR-10 for image generation.

### Output Text:
    Gazetteer: ['GAN', 'PyTorch', 'CIFAR-10']
    spaCy: ['GAN', 'PyTorch', 'CIFAR-10']
    Groq LLM: ['GAN', 'PyTorch', 'CIFAR-10', 'image generation']
    Combined (priority): ['GAN', 'PyTorch', 'CIFAR-10', 'image generation']

## Contributing

Contributions are welcome! Feel free to:

Improve the Gazetteer list

Add support for new models

Enhance tag prioritization logic
