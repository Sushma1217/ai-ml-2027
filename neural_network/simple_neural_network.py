import math
from activation_functions import sigmoid, relu

X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y = [0, 0, 0, 1]  # all actual answers
w1 = [0.5, 0.4]
b1 = 0.1

w2 = [0.2, 0.7]
b2 = 0.2

# outout weights
w_out = [0.6, 0.3]
b_out = 0.1

learning_rate = 0.1
epochs = 1000

# Forward pass
def forward(x):
    z1 = x[0] * w1[0] + x[1] * w1[1] + b1
    a1 =  relu(z1)
    z2 = x[0] * w2[0] + x[1] * w2[1] + b2
    a2 = relu(z2)
    z_out = a1 * w_out[0] + a2 * w_out[1] + b_out
    prediction = sigmoid(z_out)
    return prediction, z1, a1, z2, a2, z_out

# Training

# X[i]        → input
# forward()   → prediction
# y[i]        → actual answer
# prediction + y[i] → loss

for epoch in range(epochs):

    total_loss = 0

    for i in range(len(X)):

        # -----------------------------
        # 1. Forward pass
        # -----------------------------

        prediction, z1, a1, z2, a2, z_out = forward(X[i])

        target = y[i]

        # -----------------------------
        # 2. Calculate loss
        # -----------------------------

        loss = -(
            target * math.log(prediction + 1e-8)
            + (1 - target) * math.log(1 - prediction + 1e-8)
        )

        total_loss += loss

        # -----------------------------
        # 3. Backpropagation
        # -----------------------------

        # Loss -> output prediction
        d_loss_d_prediction = (
            -(target / (prediction + 1e-8))
            + ((1 - target) / (1 - prediction + 1e-8))
        )

        # Prediction -> z_out
        d_prediction_d_zout = prediction * (1 - prediction)

        # Combined gradient for output neuron
        d_loss_d_zout = (
            d_loss_d_prediction
            * d_prediction_d_zout
        )

        # -----------------------------
        # Gradients for output weights
        # -----------------------------

        gradient_w_out_1 = d_loss_d_zout * a1
        gradient_w_out_2 = d_loss_d_zout * a2
        gradient_b_out = d_loss_d_zout

        # -----------------------------
        # Gradients flowing into hidden layer
        # -----------------------------

        d_loss_d_a1 = d_loss_d_zout * w_out[0]
        d_loss_d_a2 = d_loss_d_zout * w_out[1]

        # ReLU derivative
        if z1 > 0:
            d_a1_d_z1 = 1
        else:
            d_a1_d_z1 = 0

        if z2 > 0:
            d_a2_d_z2 = 1
        else:
            d_a2_d_z2 = 0

        # Gradients for hidden neurons
        d_loss_d_z1 = d_loss_d_a1 * d_a1_d_z1
        d_loss_d_z2 = d_loss_d_a2 * d_a2_d_z2

        # -----------------------------
        # Gradients for hidden weights
        # -----------------------------

        gradient_w1_0 = d_loss_d_z1 * X[i][0]
        gradient_w1_1 = d_loss_d_z1 * X[i][1]
        gradient_b1 = d_loss_d_z1

        gradient_w2_0 = d_loss_d_z2 * X[i][0]
        gradient_w2_1 = d_loss_d_z2 * X[i][1]
        gradient_b2 = d_loss_d_z2

        # -----------------------------
        # 4. Gradient descent
        # -----------------------------

        # Output neuron
        w_out[0] -= learning_rate * gradient_w_out_1
        w_out[1] -= learning_rate * gradient_w_out_2
        b_out -= learning_rate * gradient_b_out

        # Hidden neuron 1
        w1[0] -= learning_rate * gradient_w1_0
        w1[1] -= learning_rate * gradient_w1_1
        b1 -= learning_rate * gradient_b1

        # Hidden neuron 2
        w2[0] -= learning_rate * gradient_w2_0
        w2[1] -= learning_rate * gradient_w2_1
        b2 -= learning_rate * gradient_b2

    # -----------------------------
    # Average loss for this epoch
    # -----------------------------

    average_loss = total_loss / len(X)

    if epoch % 100 == 0:
        print(
            "Epoch:",
            epoch,
            "Loss:",
            average_loss
        )


# -----------------------------
# Final predictions
# -----------------------------

print("\nFinal predictions:")

for i in range(len(X)):

    prediction, _, _, _, _, _ = forward(X[i])

    print(
        X[i],
        "Actual:",
        y[i],
        "Prediction:",
        prediction
    )

