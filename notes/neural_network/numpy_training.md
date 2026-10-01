1. Batch loss

Loss calculated across multiple examples rather than one example.

2. Mean loss

Average loss across the batch.

3. Vectorized training

Using NumPy arrays instead of manually processing every value.

4. Gradient shapes

Start noticing that gradients have the same shape as the parameters they update.

For example:

weights_hidden.shape
↓
gradient_weights_hidden.shape

This will become very important when we move to PyTorch.
