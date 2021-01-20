# Random Walk Simulation
import numpy as np 

#Set your seed
np.random.seed(123)

# Initialize all_walks
all_walks = []

#Simulate random walk 10 times
for i in range(10)

# Random walks for loop
random_walk = [0]
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)
all_walks.append(random_walk)

# Print random_walk
#print(random_walk)
print(all_walks)

#Visualize the random_walk
import matplotlib.pyplot as plt 

#Plot random walk
plt.plot(random_walk)

#Display plot
plt.show()

#Further plots
#Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

#Plot np_aw and show
plt.plot(np_aw)
plt.show()
#Plots every run and creates messy figure

#Clear the figure
plt.clf()

#Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

#Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()