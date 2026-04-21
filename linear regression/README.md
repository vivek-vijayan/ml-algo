# Linear Regression

A C++ implementation of linear regression using gradient descent optimization. This project demonstrates the fundamental concepts of machine learning with a simple yet effective approach to fitting a linear model to data.

## Overview

This implementation trains a linear regression model on a dataset using the gradient descent algorithm. The model learns optimal weight (w) and bias (b) parameters to minimize the mean squared error between predicted and actual values.

## Features

- **CSV Data Loading**: Reads training data from a CSV file
- **Gradient Descent Optimization**: Iteratively updates model parameters to minimize loss
- **Mean Square Error (MSE)**: Loss function for regression tasks
- **Real-time Monitoring**: Prints loss and model parameters at regular intervals
- **Prediction**: Make predictions on new data using the trained model

## Requirements

- C++11 or higher
- Standard C++ library (iostream, vector, fstream, sstream)
- A C++ compiler (g++, clang, or equivalent)

## File Structure

```
linear regression/
├── cpp/
│   ├── main.cc          # Main implementation file
│   ├── dataset.csv      # Training dataset
│   └── output.txt       # Training output logs
└── README.md            # This file
```

## Dataset Format

The dataset should be a CSV file with two columns:
- **Column 1**: Input feature (X)
- **Column 2**: Target output (Y)

Example:
```
100,10000
200,20000
300,30000
400,40000
```

## Building the Project

### Using g++:
```bash
g++ -std=c++11 -o linear_regression main.cc
```

### Using clang:
```bash
clang++ -std=c++11 -o linear_regression main.cc
```

## Running the Project

1. Update the dataset path in `main.cc` at line 110 to point to your CSV file
2. Run the compiled executable:
```bash
./linear_regression
```

### Example Output:
```
Linear Regression Execution
Loading file : /path/to/dataset.csv
Total rows : 100
Epoch: 0 Loss: 1234.56 w: 1.05 b: 1.1
Epoch: 100 Loss: 567.89 w: 75.3 b: 50.2
...
Predicted Value for 800 : Rs.60500
```

## Algorithm Details

### Linear Model
The model uses the equation: **ŷ = w·x + b**

Where:
- **ŷ** = predicted value
- **w** = weight (slope)
- **b** = bias (intercept)
- **x** = input feature

### Gradient Descent
The algorithm updates parameters iteratively:

**w := w - lr × ∂L/∂w**
**b := b - lr × ∂L/∂b**

Where:
- **lr** = learning rate (0.00000001 in current implementation)
- **∂L/∂w, ∂L/∂b** = gradients of loss function

### Loss Function
Mean Squared Error (MSE):
**L = (1/n) × Σ(y - ŷ)²**

## Key Parameters

- **Learning Rate**: 1e-8 (configured in `learn()` function)
- **Epochs**: 10,000,000,000 (configurable in `main()`)
- **Initial Weights**: w = 1.0, b = 1.0

## Code Structure

### Main Functions

- **`load_csv(path)`**: Loads training data from CSV file
- **`learn(dataset, epochs)`**: Trains the model using gradient descent
- **`predict(model, input)`**: Makes predictions using trained model
- **`mean_square_error(y, yh)`**: Calculates MSE for a single sample

### Type Definitions (Macros)

```cpp
#define scalar double
#define feature std::vector<scalar>
#define matrix std::vector<feature>
#define model std::pair<double, double>  // <w, b>
```

## Example Usage

```cpp
// Load data
const matrix dataset = load_csv("dataset.csv");

// Train model for 10 billion epochs
const model trained_model = learn(dataset, 10000000000);

// Make a prediction
double prediction = predict(trained_model, 800);
std::cout << "Predicted Value: " << prediction << std::endl;
```

## Notes

- The current learning rate is very small (1e-8) to ensure stable training
- Adjust epochs based on your dataset size and convergence requirements
- The CSV file path must be absolute or relative to the working directory
- Loss values are printed every 100 epochs for progress monitoring


## Author

Created as part of the ml-algo project by Vivek Vijayan
