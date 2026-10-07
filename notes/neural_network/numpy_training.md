for learning rate .1
Epoch: 0 Loss: 0.8462449430983792
Epoch: 100 Loss: 0.38218327404414176
Epoch: 200 Loss: 0.19900315993804413
Epoch: 300 Loss: 0.10351287154118735
Epoch: 400 Loss: 0.06461062847914466
Epoch: 500 Loss: 0.04531843383940205
Epoch: 600 Loss: 0.034574506054623456
Epoch: 700 Loss: 0.027833296138044836
Epoch: 800 Loss: 0.023321371112669794
Epoch: 900 Loss: 0.02006448325974261

for learning rate 0.01
Epoch: 0 Loss: 0.8462449430983792
Epoch: 100 Loss: 0.6388044617566242
Epoch: 200 Loss: 0.5758430363584334
Epoch: 300 Loss: 0.5409113801423209
Epoch: 400 Loss: 0.5147256160244883
Epoch: 500 Loss: 0.49182518326692637
Epoch: 600 Loss: 0.4698458493591696
Epoch: 700 Loss: 0.44798643087235446
Epoch: 800 Loss: 0.42605786857552225
Epoch: 900 Loss: 0.40408915424751635

for learning rate 0.5
Epoch: 0 Loss: 0.8462449430983792
Epoch: 100 Loss: 0.04509755712162541
Epoch: 200 Loss: 0.017454959392007963
Epoch: 300 Loss: 0.010772302310911445
Epoch: 400 Loss: 0.007656686562362837
Epoch: 500 Loss: 0.005959762671643985
Epoch: 600 Loss: 0.0048575488195842665
Epoch: 700 Loss: 0.004104854996927781
Epoch: 800 Loss: 0.003533915657745462
Epoch: 900 Loss: 0.003108986426992574

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
