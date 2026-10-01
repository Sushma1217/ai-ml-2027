What is it?

Until now, we wrote things manually:

z1 = x[0] _ w1[0] + x[1] _ w1[1] + b1

But real neural networks don't calculate every neuron using separate lines. They use vectors and matrices to represent inputs and weights and perform these calculations together.

Why do we need it?

Because your current approach becomes impossible to manage when you have:

100 inputs
100 neurons
10 layers
millions of parameters

This is also the bridge between your NumPy learning and real neural networks/PyTorch.

Where does it fit?
Individual neuron calculations
↓
Multiple neurons
↓
Vectors & matrices ← TODAY
↓
NumPy neural network
↓
PyTorch tensors
↓
Real Deep Learning
🟢 Part 1 — Understand a vector

You already used this:

x = [2, 3]

Think of it as:

x = [x1, x2]

This is a vector.

Instead of writing:

x1 = 2
x2 = 3

we can represent them together:

x = [2, 3]

You've actually already used vectors without calling them that.

🟢 Part 2 — Understand weights as a vector

You currently have:

w1 = [0.5, 0.4]

This means:

w1 = [weight for x1, weight for x2]

So:

x = [2, 3]
w1 = [0.5, 0.4]

The calculation:

x[0] _ w1[0] + x[1] _ w1[1]

is called a dot product.

🟢 Part 3 — Learn dot product

This is the only maths concept I want you to learn today.

Don't think of it as scary maths.

For:

x = [2, 3]

w = [0.5, 0.4]

dot product simply means:

(2 × 0.5) + (3 × 0.4)

which gives:

1.0 + 1.2 = 2.2

That's it.

So:

x[0] _ w[0] + x[1] _ w[1]

can be written using NumPy as:

np.dot(x, w)
Remember:

Dot product = multiply corresponding values and add them together.

Old approach
z1 = x[0] _ w1[0] + x[1] _ w1[1] + b1
z2 = x[0] _ w2[0] + x[1] _ w2[1] + b2
Vector/matrix approach
z = np.dot(weights, x) + bias

Same concept.The second approach simply allows us to handle many values efficiently.

Vector = list of numbers

Matrix = collection of vectors/numbers

Dot product = multiply corresponding values and add

Shape = tells us dimensions

Matrix multiplication = allows many neuron calculations together
