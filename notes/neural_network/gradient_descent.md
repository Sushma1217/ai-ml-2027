Gradient Descent is the method used to adjust the model's weights so that the loss becomes smaller.

The closer the weight gets to the target, the smaller the loss becomes.
This is the intuition we need.

What problem does Gradient Descent solve? 2. What is a gradient, in simple words?
it tell us how to adjust the weight to make the loss smaller

3. What is a learning rate?
   it is the hyperparameter that controls the stepsize of model that takes along the loss gradient to update its weight during optimization.

4. What happens if the learning rate is too small?
   model takes tiny steps, learning is very slow

5. What might happen if the learning rate is too large?
   very large steps
   → may overshoot the minimum
   → loss can bounce around or even diverge

6. What did you observe about the loss after each iteration?
   loss is value is increasing with each iternation
