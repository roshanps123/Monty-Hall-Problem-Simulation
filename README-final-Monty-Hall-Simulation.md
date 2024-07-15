# Monty Hall Simulation
This Python script simulates the Monty Hall problem, a famous probability puzzle involving doors, a car, and goats. The script allows you to specify the number of doors (n) and the number of cars (k) to perform the simulation and calculate the probabilities of winning by switching doors or sticking with the initial choice. Additionally, the script generates a 3D surface plot visualizing the ratio of the switching win probability to the sticking win probability for different combinations of n and k.

# Requirements
To run this script, you'll need the following Python packages:

NumPy

Matplotlib
# Running the Script
1. Save the code in a Python file (e.g., monty_hall.py).

2. Open a terminal or command prompt and navigate to the directory where the file is saved.

Run the script by executing the following command:python monty_hall.py

3. The script will prompt you to enter the number of doors (n) and the number of cars (k). Make sure to enter valid values where n is greater than k + 1, and both n and k are positive integers.

4. After entering the input values, the script will run the simulation with 100,000 trials and print the following results:

   Probability of winning by sticking with the initial choice
   
   Probability of winning by switching doors
   
5. Ratio of the switching win probability to the sticking win probability

6. Additionally, the script will generate a 3D surface plot showing the ratio of the switching win probability to the sticking win probability for different combinations of n (number of doors) and k (number of cars).

# Understanding the Output
1. Probability of winning with sticking: The probability of winning the game by sticking with the initial choice.
2. Probability of winning with switching: The probability of winning the game by switching doors after the host reveals a door with a goat.
3. Ratio of probability for switching to sticking: The ratio of the switching win probability to the sticking win probability.
4. The 3D surface plot visualizes the ratio of the switching win probability to the sticking win probability for different values of n (number of doors) and k (number of cars). The higher the ratio, the more advantageous it is to switch doors.
