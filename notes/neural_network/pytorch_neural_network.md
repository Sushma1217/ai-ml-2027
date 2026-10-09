# optimizer

The optimizer takes the gradients calculated by backward() and updates the model's weights.

loss.backward()
↓
calculate gradients

optimizer.step()
↓
update weights

# PyTorch Neural Network

## 1. nn.Module

nn.Module is PyTorch's base class for building neural networks.
Instead of manually keeping track of weights and biases, PyTorch can manage them for us.

## 2. nn.Linear

nn.Linear(in_features,out_features,bias=True)
applies an linear trasnformation to the incoming data

## 3. Forward Pass

it is the process where input flows through the input payer to output layer and generate the prediction in neural network

## 4. BCELoss

pytorch function or method for binar cross entropy loss prediction

## 5. Optimizer

the optimizer takes the gradients calculated by backward() and updates the model's weights.

## 6. Training Loop

the reapeted process of Forward pass, calculate the loss, backpropogation, calculate gradients, Update weights is called training loop.

## 7. optimizer.zero_grad()

pytorch stores the gradients, so we use zero_grand() to clear the previous ones to before calculating new ones.

## 8. loss.backward()

a method of pytorch used for backpropogation.

## 9. optimizer.step()

a function that actually updates the weights in the model

## 10. Final Prediction

end result of prediction

## 11. Manual Neural Network vs PyTorch

manaully we have to calculate forward pass, loss, backpropogation activation fucntion, hidden layer, weights of output layer, updating those to the training values etc using heavy maths but pytorch replaces it using a simple methods like relu(), sigmod(), optimizer etc so it wil be east to handle to larger set of data.
