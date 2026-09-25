import math 

x1 = 2.0
x2 = 3.0

w1 = 0.5
w2 = 0.4

b = 0.1

target = 1.0 #target → correct answe

# Calculate weighted sum
z = x1 * w1 + x2 * w2 + b

print("z:", z)

# Step 4 — Apply sigmoid
prediction = 1 / (1 + math.exp(-z))

print("prediction:", prediction) #The prediction will be approximately:0.909 so 90.9% probability of class 1.

# Calculate loss For today, use the simple squared-error loss:
loss = (prediction-target)**2
print("loss:", loss) # 0.008 the loss is small because you see the target is 1 and prediction is .909


# Calculate the gradients - dnt worry about the formulas
d_loss_d_prediction = 2 * (prediction - target)

d_prediction_d_z = prediction * (1 - prediction)

d_z_d_w1 = x1
d_z_d_w2 = x2

# Now combine them:
gradient_w1 = (
    d_loss_d_prediction
    * d_prediction_d_z
    * d_z_d_w1
)

gradient_w2 = (
    d_loss_d_prediction
    * d_prediction_d_z
    * d_z_d_w2
)

print("gradient_w1:", gradient_w1) #-0.030
print("gradient_w2:", gradient_w2) #-0.0452

learning_rate =.1
w1 = w1 - learning_rate * gradient_w1
w2 = w2 -learning_rate *gradient_w2

print("updated w1:", w1) #0.503
print("updated w2:", w2) #0.404


# task
xx1 = 3.0
xx2 = 2.0
ww1 = .6
ww2 = .3
bias = .25
target = 1.0

# Calculate z
zz = xx1 * ww1 + xx2 * ww2 + bias

# Calculate predcition using sigmod
task2_prediction = 1 / (1 + math.exp(-zz))
print("task2_prediction:", task2_prediction) #0.934

# Calculate loss
task2_loss = (task2_prediction-target)**2
print("task2_loss:", task2_loss) #0.00435
 
# Calculate the three intermediate gradients:
task2_loss_d_prediction = 2 * (task2_prediction - target) 

task2_prediction_d_z = task2_prediction * (1 - task2_prediction)

task2_z_d_w1 = xx1
task2_z_d_w2 = xx2

# Now combine them:
task2_gradient_w1 = (
    task2_loss_d_prediction
    * task2_prediction_d_z
    * task2_z_d_w1
)

task2_gradient_w2 = (
    task2_loss_d_prediction
    * task2_prediction_d_z
    * task2_z_d_w2
)

print("task2_gradient_w1:", task2_gradient_w1)  #-0.0244
print("task2_gradient_w2:", task2_gradient_w2) #-0.0162

# Update weights
learning_rate =.1
ww1 = ww1 - learning_rate * task2_gradient_w1
ww2 = ww2 -learning_rate *task2_gradient_w2

print("updated ww1:", ww1) #0.600
print("updated ww2:", ww2) #0.301

