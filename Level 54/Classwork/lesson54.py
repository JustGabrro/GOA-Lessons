import numpy as np

example_input = [1, 0.2, 0.1, 0.05, 0.2]
example_weights = [0.2, 0.12, 0.4, 0.6, 0.9]

# Duplicate example_input
example_input *= 2
print(f"example_input*2 = {example_input}")

# Convert example_input to numpy array
input_vector = np.array(example_input)
print(f"input_vector = {input_vector}")

# Multiply input_vector by 2
input_vector *= 2
print(f"input_vector*2 = {input_vector}")

# Convert example_weights to numpy array
weights = np.array(example_weights)

bias_weight = 0.2
activation_level = np.dot(input_vector, weights) + (bias_weight * 1)
print(f"activation_level = {activation_level}")

threshold = 0.5
if activation_level >= threshold:
    perceptron_output = 1
else:
    perceptron_output = 0

print(f"perceptron_output = {perceptron_output}")

# Adjust weights based on expected_output
expected_output = 1
learning_rate = 0.1  # Example learning rate

# Update weights
new_weights = weights + learning_rate * expected_output * input_vector
print(f"new_weights = {new_weights}")



# Sample data and expected results for testing
sample_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

expected_results = [0, 0, 0, 1]  # Example expected results (AND gate)

# Initial weights and bias
weights = [0.0, 0.0]
bias_weight = 0.0

# Activation threshold
activation_threshold = 0.5

for iteration_num in range(5):  # Run for 5 iterations
    correct_answers = 0
    
    for idx, sample in enumerate(sample_data):
        input_vector = np.array(sample)
        weights = np.array(weights)
        
        # Calculate activation level
        activation_level = np.dot(input_vector, weights) + (bias_weight * 1)
        
        # Determine perceptron output
        if activation_level >= activation_threshold:
            perceptron_output = 1
        else:
            perceptron_output = 0
        
        # Check if the output matches the expected result
        if perceptron_output == expected_results[idx]:
            correct_answers += 1
        
        # Update weights and bias
        new_weights = []
        for i, x in enumerate(sample):
            new_weights.append(weights[i] + (expected_results[idx] - perceptron_output) * x)
        
        bias_weight = bias_weight + ((expected_results[idx] - perceptron_output) * 1)
        weights = np.array(new_weights)
    
    # Print the number of correct answers for the iteration
    print('{} correct answers out of 4, for iteration {}'.format(correct_answers, iteration_num))
