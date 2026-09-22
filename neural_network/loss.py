import math

def binary_class_entropy(actual, prediction ):
    # Prevent log(0) errors if prediction is exactly 0 or 1
    epsilon = 1e-15
    prediction = max(epsilon, min(1 - epsilon, prediction))
    
    # BCE Formula for a single value: -[y * log(p) + (1 - y) * log(1 - p)]
    loss = -(actual * math.log(prediction) + (1 - actual) * math.log(1 - prediction))
    return loss


print("binary_class_entropy for 1,.9",binary_class_entropy(1,.9))
print("binary_class_entropy for 1,.2",binary_class_entropy(1,.2))

# Try the opposite case
print("binary_class_entropy for 0,.1",binary_class_entropy(0,.1))
print("binary_class_entropy for 0,.8",binary_class_entropy(0,.8))