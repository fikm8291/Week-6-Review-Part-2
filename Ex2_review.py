# -------------------------------------------
# Exercise 2: Revision
# -------------------------------------------
# In this exercise, you’ll work in pairs or groups of 3
# to revise the core Python concepts so far:
# - Variables & input()
# - if/elif/else
# - for & while loops
# - Introduction to basic string methods (.lower(), .strip())
# - Using Git to collaborate
#
# IMPORTANT:
# • You will all use ONE computer per task.
# • You will SWAP LEARNERS (the person typing) after each STEP, but stay at the same computer.
# • You will SWAP COMPUTERS only after each full TASK.
# -------------------------------------------


# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Each group shares one GitHub Classroom repository.
#
# For each TASK:
# - Stay at the same computer.
# - Swap who is typing after each STEP.
# - After completing the whole task:
#     1. Save your file
#     2. git add, commit, and push
#     3. Move to the next computer in your group
#     4. git pull origin main on that computer and continue
#
# Example commands:
# git add Ex2_review.py
# git commit -m "Completed Task 1"
# git push origin main
# (Next computer) git pull origin main
# -------------------------------------------


# Task 1: Greeting Program
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Greeting Program\n"
    + "-------------------------------------------")

# Step 1:
# -------------------------------------------
# Ask the user for their name using input().
# The .strip() method: removes extra spaces at the start or end of a string.
# Example:
#   name = "  Alice  ".strip()
#   print(name)  # Output: "Alice"
# Use .strip() on the user input and store it in a variable called name.
# Print: "Welcome, <name>!"
#
# Write your code below:



# Step 2:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Ask the user for their age.
# Use int() to convert it into a number because input() returns text.
# Print: "You are <age> years old — great to have you here!"
#
# Write your code below:



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 1 - greeting program"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull origin main
# -------------------------------------------


# Task 2: Colour & Mood Checker
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Colour & Mood Checker\n"
    + "-------------------------------------------")

# Step 1:
# -------------------------------------------
# Ask the user for their favourite colour.
# The .lower() method: converts text to lowercase for easier comparisons.
# Example:
#   colour = "Blue".lower()
#   print(colour)  # Output: "blue"
# Use .lower() on the input and store it in a variable called colour.
#
# Write your code below:



# Step 2:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Use if/elif/else to respond to the colour:
# - "blue" → "Cool choice!"
# - "yellow" → "Bright and happy!"
# - Otherwise → "That's a unique colour!"
#
# Write your code below:



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 2 - colour & mood checker"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull origin main
# -------------------------------------------


# Task 3: Number Table & Loop Practice
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Number Table & Loop Practice\n"
    + "-------------------------------------------")

# Step 1:
# -------------------------------------------
# Ask the user to enter a number between 1 and 10.
# Convert it to an integer using int() and store it in a variable.
#
# Write your code below:



# Step 2:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Use a for loop to print the multiplication table for that number (1 to 10).
# Example output:
# 3 x 1 = 3
# 3 x 2 = 6
#
# Write your code below:



# Step 3:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Ask the user if they want to try another number ("yes"/"no").
# Use a while loop to repeat the multiplication table while the user answers "yes".
# Use .lower() to make sure input like "YES" or "Yes" works.
#
# Write your code below:



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 3 - number loops"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Now that everyone has had a turn, continue swapping computers
# after each extension task as before.

# Extension 1: Mini Profile Program
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Mini Profile Program\n"
    + "-------------------------------------------")

# Step 1:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Remember to run:
#   git pull origin main
# Ask the user for their first name and favourite number.
# Use .lower() on the name and combine it with the number to create a username.
# Print the username.
#
# Write your code below:



# Step 2:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Ask the user for three test scores.
# Convert each score to an integer.
# Calculate and print the average score.
#
# Write your code below:



# Step 3:
# -------------------------------------------
# SWAP LEARNERS BEFORE THIS STEP (STAY AT THE SAME COMPUTER)
# Use if/elif/else to give feedback:
# - 70 or more → "Excellent!"
# - 50–69 → "Good effort!"
# - below 50 → "Needs improvement."
#
# Write your code below:



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 4 - profile program"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# Work together on one computer for this challenge.
# You will combine all the skills learned so far into a single "Student Helper" program.
#
# GOAL:
# Build an interactive program with a menu that loops until the user chooses to exit.
# The program should allow the user to:
#   1. Create a username
#   2. Check average test scores
#   3. Exit the program
#
# GUIDANCE / STEP-BY-STEP:
#
# Step 1: Greeting
# -------------------------------------------
# Ask the user for their name.
# Use .strip() to remove extra spaces.
# Print a welcome message using their name.
#
# Example:
# Enter your name:   Alice
# Output: "Welcome, Alice!"
#
# Step 2: Display Menu
# -------------------------------------------
# Use a while loop to repeatedly show the menu until the user chooses to exit.
# Menu example:
# 1. Create a username
# 2. Check average test scores
# 3. Exit
# Ask the user to choose an option.
#
# Step 3: Option 1 – Create a Username
# -------------------------------------------
# IF the user enters "1", ask the user for their first name and favourite number.
# Use .lower() on the name to make the username lowercase.
# Combine the name and number and print it.
#
# Example:
# Enter first name: Bob
# Enter favourite number: 7
# Output: "Your username could be: bob7"
#
# Step 4: Option 2 – Average Test Scores
# -------------------------------------------
# ELIF the user enters "2", ask the user to enter three test scores.
# Use int() to convert each input into a number.
# Calculate the average score.
# Print the average and give feedback:
#   70 or more → "Excellent!"
#   50–69 → "Good effort!"
#   Below 50 → "Needs improvement."
#
# Step 5: Option 3 – Exit
# -------------------------------------------
# ELIF the user enters "3", print a goodbye message and stop the program.
#
# Step 6: Input Validation (Bonus)
# -------------------------------------------
# - Ensure the menu choice is 1, 2, or 3. Otherwise (i.e. ELSE), ask again.
# - Ensure test scores are between 0 and 100.
# - You can add extra features like asking for the user's age, storing usernames, or looping back to the menu after each task.
#
# Example Output:
# -------------------------------------------
# Welcome, Alice!
# Menu:
# 1. Create a username
# 2. Check average test scores
# 3. Exit
# Enter your choice: 1
# Enter first name: Alice
# Enter favourite number: 5
# Your username could be: alice5
# (Menu shows again until user chooses 3)
#
# Write your code below:



# FINAL SUBMISSION
# -------------------------------------------
# Once your group completes all tasks:
# 1. Save your file
# 2. git add Ex2_review.py
# 3. git commit -m "Completed all activities"
# 4. git push origin main
# 5. Check GitHub to confirm your final version
# -------------------------------------------
