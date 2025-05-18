# Neural Network Dependency Parser

This project implements a transition-based dependency parser using an arc-standard transition system and a feed-forward neural network in PyTorch. It supports training and evaluation on CoNLL-formatted datasets.


## Project Structure

```text
├── data/
│   └── download_data.py  # Script to download required datasets
├── parser/
|   ├── conll_reader.py  # Functions to read CoNLL formatted data
|   ├── decoder.py  # Decoder implementing arc-standard transitions
|   ├── extract_training_data.py  # Extract training instances from parsed data
│   └── get_vocab.py  # Vocabulary utilities for words, POS tags, labels
├── train/
|   ├── train_model.py  # Script to train the neural parser model
│   └── evaluate.py  # Evaluate trained models on test data
├── requirements.txt
├── README.md
└── .gitignore
```
## Features

- Arc-standard transition system for dependency parsing
- Feed-forward neural network implementation using PyTorch
- Training and evaluation pipeline with accuracy metrics
- Dataset download script via `gdown`
- Easy extensibility for additional features or parsing strategies

## Usage

### Requirements:
- Python 3.x
- PyTorch
- Any other dependencies listed in requirements.txt

Install dependencies with:
```python
pip install -r requiements.txt
```

### Run the Project:
#### 1. Download Data
Run the dataset download script:
```python
python data/download_data.py
```

#### 2. Training the Model
Run the training script:
```python
python train/train_model.py
```

#### 3. Evaluating the Model
```python
python train/evaluate.py
```
### Notes
- Make sure to place or download all necessary datasets in the data/ directory before running training or evaluation scripts.
- Install all dependencies listed in requirements.txt to ensure the environment is properly set up.
- The code expects input data in CoNLL format for training and evaluation.
- You can adjust hyperparameters and file paths directly in the scripts if needed.
- Model checkpoint files (if generated) are not tracked by Git thanks to .gitignore.
- It’s recommended to run the code in a Python virtual environment to avoid dependency conflicts.
- Future improvements could include modularizing the code further by separating model architecture, data processing, and training logic into distinct modules for better scalability and easier testing.

