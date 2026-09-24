weight = 0.5
# weight = 0.8
# weight = 0.95

target = 1.0

#  Our goal is simply: Move weight from 0.5 toward 1.0. -->
loss = (weight - target)**2 # its square. "How far is my current weight from the target?"

# <!-- Calculate the loss -->
print("loss",loss) 
# Is the loss large or small? -  no its small .25 for weight 0.5
# Is the loss large or small? - yes its comparitively large .64 for weight 0.8
# Is the loss large or small? - yes its  large .90 for weight .95

#  Now introduce the "gradient"
gradient = 2*(weight -target) #no need that from where the 2 came
# The gradient tells us the direction in which the loss is changing.

learning_rate = 0.1

weight = weight - learning_rate * gradient
print("weight after",weight) #.6
print("gradient",gradient) #-1.0
print("loss",loss) #.25

# Repeat the update- Now put the calculation inside a loop.
for i in range(20):
    # 1. Calculate loss (how far off we are from the target)
    loss = (weight - target)**2
    # 2. Calculate gradient (direction and rate of change)
    gradient = 2*(weight -target)
    # 3. Update weight (move in opposite direction of gradient)
    weight = weight - learning_rate * gradient
    print(f"Iteration {i+1}: weight={weight:.4f}| gradient = {gradient:.4f} | loss = {loss:.4f}") #.4f is to limit the float value to 4 digit




