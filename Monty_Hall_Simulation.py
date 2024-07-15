import random
import numpy as np
import matplotlib.pyplot as plt

# Number of doors
n=5

# Number of Cars
k=1

# Number of Trials
num_trials=100000

# Function for Performing Monty Hall Simulation
def monty_hall_simulation(num_trials=1000 , n=3, k=1):

    # Variables for storing number of wins with switching and sticking approach
    wins_switch = 0
    wins_stick = 0

    # Performing all Trials
    for i in range(num_trials):

        # K randomly choosen doors with cars behind
        winning_doors = random.sample(range(1, n + 1), k)

        # Door chosen by contestant
        selected_door = random.randint(1, n)

        # Calculating wins with Sticking
        if selected_door in winning_doors:
            wins_stick += 1

        # Doors with Goats behind them
        losing_doors = []
        for door in range(1, n + 1):
            if door not in winning_doors:
                losing_doors.append(door)

        # Removing Selected door from Losing doors
        if selected_door in losing_doors:
            losing_doors.remove(selected_door)

        # Revealed Door by Host
        host_door = random.choice(losing_doors)

        # Doors available for switching
        remainning_doors = []
        for door in range(1, n + 1):
            if door != selected_door and door != host_door:
                remainning_doors.append(door)

        # Switched Door
        switched_door = random.choice(remainning_doors)

        # Calculating wins with Switching
        if switched_door in winning_doors:
            wins_switch += 1

    # Calculating Sticking and Switching Probabilities
    probability_win_stick=wins_stick/num_trials
    probability_win_switch=wins_switch/num_trials

    return probability_win_stick ,probability_win_switch

# Checking for Valid Inputs

if(n>k+1 and n>0 and k>0):

  probability_win_stick,probability_win_switch = monty_hall_simulation(num_trials ,n, k)

  # Printing all the results obtained
  print('Monty Hall Problem with {} doors with {} of the doors having cars\n'.format(n, k))
  print('Probability of winning with sticking : {:.2f}'.format(probability_win_stick))
  print('Probability of winning with switching: {:.2f}'.format(probability_win_switch))
  print('Ratio of probability for switching to sticking: {:.2f}'.format(probability_win_switch / probability_win_stick))

else:

  print('Please Enter valid values of n and k (n,k>0 and n>k+1)')


# Surface Plot

# Range of values for number of doors
n_values = np.arange(4, 12)

# Range of values for number of cars
k_values = np.arange(1, 8)

# Initialize an empty matrix to store the probability ratios
ratio_matrix = np.zeros((len(n_values), len(k_values)))

# Calculate the ratios for all combinations of n and k
for i, n in enumerate(n_values):
    for j, k in enumerate(k_values):
        if k < n-1:  # Ensure k is less than or equal to n
            probability_win_stick, probability_win_switch = monty_hall_simulation(num_trials, n, k)
            ratio_matrix[i, j] = probability_win_switch / probability_win_stick
        else:
            ratio_matrix[i, j] = float('nan')  # Set ratio to NaN if k > n

# Create a meshgrid of n and k values
n_mesh, k_mesh = np.meshgrid(n_values, k_values)

# Plot the surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(n_mesh.T, k_mesh.T, ratio_matrix, cmap='viridis')
ax.set_xlabel('Number of doors (n)')
ax.set_ylabel('Number of cars (k)')
ax.set_zlabel('Ratio of P(win|W) to P(win|T)')
ax.set_title('Monty Hall Simulation: Ratio of Winning Probabilities')
ax.grid(True, color=['red', 'yellow'], linestyle='--')
plt.show()