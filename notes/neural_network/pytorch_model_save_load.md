In real projects, you need to save a trained model and load it later without training it again.
This connects your neural network training knowledge to a practical ML workflow: train once, save the model, and use it to make new predictions.

model.state_dict()
Returns the model's learned parameters, such as weights and biases. We save these instead of retraining the model each time.

torch.save() and load_state_dict()
Save the learned parameters to a file and load them into a model with the same architecture.

model.eval() and torch.no_grad()
model.eval() switches the model to evaluation mode. torch.no_grad() prevents gradient tracking during prediction, saving unnecessary computation and memory.

Why model persistence is needed.
model persistence means saving the trained model into a file(like .pt, .pkl, .h5) so we can reuse it later.
it is needed to avoid the retraining, portability(deplpy across different env, easily share among teammates),
deployment

What state_dict() contains.
it contains hidden.weight, hidden.bias, output.weight and output.bias

Difference between saving a model's parameters and saving its architecture
saving model's params - saves only weights, biases that model learnt during the training
saving architecure - it saves blueprint/structure of the model(how the layers are connected,activiation function used) so we can use the saved model anytime

How torch.save() and load_state_dict() work.
torch.save()- will the learned parameters like weights and biases to a file.
load_state_dict()- will take the learned params from the file and load them when we initialize the model.

Difference between model.eval() and torch.no_grad().
model.eval() - evaluate the model
torch.no_grad() - It prevents gradient tracking for operations inside the block for saving unnecessary computation and memory; it does not clear previously stored gradients

Training versus inference
Training - learning phase. the model processed the data, calculate errors, and update its weights and biases via backpropogation
inference - application phase, model applied the learned params to prediction new unseen data.

What you observed in your experiments.
answered already with respect to the questions already.
