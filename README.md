# Neural Dependency Parser

This repository contains a PyTorch implementation of a transition-based dependency parser using the arc-standard system. It includes code for training and evaluating the parser on CoNLL-formatted data.

## Project Structure
├── data/
│   ├── train.conll
│   ├── dev.conll
|   ├── test.conll
│   └── sec0.conll
├── model/
│   └── parser_model.py
├── utils/
│   └── conll_utils.py
├── download_data.py
├── train.py
├── evaluate.py
├── requirements.txt
└── README.md

## Features

- Arc-standard transition system for dependency parsing
- Feed-forward neural network implementation using PyTorch
- Training and evaluation pipeline with accuracy metrics
- Dataset download script via `gdown`
- Easy extensibility for additional features or parsing strategies

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/neural-dependency-parser.git
cd neural-dependency-parser
