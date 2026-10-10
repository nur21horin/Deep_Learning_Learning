# Deep Learning Learning

A beginner-friendly deep learning practice repository focused on understanding the foundations of neural networks, perceptrons, forward propagation, and backpropagation.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow)
![License](https://img.shields.io/badge/License-Learning%20Only-9C27B0?style=for-the-badge)

</div>

## About the Author

This project is a personal learning repository created to explore the fundamentals of deep learning through practical examples and visual explanations.

It is intended for students and beginners who want to understand how neural networks work from the ground up using hands-on notebooks and simple Python implementations.

## Overview

This project is designed for learning by doing. It includes interactive notebooks and small Python examples that explain the building blocks of neural networks in a simple and visual way.

The repository covers:

- Perceptron learning and binary classification
- Forward propagation in a neural network
- Sigmoid activation and decision boundaries
- Backpropagation and gradient-based learning
- Artificial neural network (ANN) implementation
- A practical classification example with Keras

## Folder and File Structure

- `perceptron.ipynb` — perceptron-based classification using the placement dataset
- `fp.ipynb` — forward propagation example with a hidden layer and sigmoid activation
- `backword_propagation.ipynb` — backpropagation example with weight and bias updates
- `ANN.ipynb` — visualization of a simple 2-1-1 neural network
- `ANN.py` — Matplotlib script that draws a neural-network architecture diagram
- `Deep_Learning.ipynb` — Keras-based ANN example for a binary classification task
- `placement.csv` — student placement dataset used for the learning examples

## Recommended Learning Order

Follow the notebooks in this order:

1. `perceptron.ipynb` — start with the simplest binary classifier
2. `fp.ipynb` — learn forward propagation in a single hidden-layer network
3. `backword_propagation.ipynb` — understand how error flows backward to update weights
4. `ANN.ipynb` — visualize a simple neural architecture
5. `Deep_Learning.ipynb` — explore a Keras-based ANN implementation

## Neural Network Concept

A simple neural network usually follows this pattern:

- Input layer receives features
- Hidden layer transforms the data using weights and activation functions
- Output layer produces the final prediction

For example, a basic structure can be represented as:

```text
Input Layer -> Hidden Layer -> Output Layer
```

In this project, the hidden layer often uses a sigmoid activation function, while the final output can also be computed with sigmoid for binary classification.

## Dataset

The dataset in `placement.csv` contains the following columns:

- `cgpa`
- `resume_score`
- `placed` (binary target: 0 or 1)

This dataset is used to practice binary classification and visualize how a perceptron separates classes.

## Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

On Windows:

```bash
.\.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow mlxtend notebook jupyter
```

## Run the Notebook

Start Jupyter:

```bash
jupyter notebook
```

Open any notebook and run the cells in order.

## Notes

This is an educational project intended to help students understand the intuition behind deep learning concepts in a simple and approachable way. It is not a production-ready application, but a learning-focused codebase.

## License

This project is intended for learning and experimentation.
