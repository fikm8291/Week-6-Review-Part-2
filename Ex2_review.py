# -------------------------------------------
# Exercise 2: Python Revision & Collaboration
# -------------------------------------------
#
# GOAL:
# 1. Review core concepts: variables, input, logic, and loops.
# 2. Master String Methods: .lower() and .strip().
# 3. Practise the Pair Programming Workflow: Driver vs Navigator.
# 4. Sync code between team members using Git (Push & Pull).
#
# CONCEPT:
# Revision ensures your foundations are solid. We are combining everything
# you have learned with new string methods to make your code more robust.
#
# PAIR PROGRAMMING RULES:
# - The DRIVER types the code.
# - The NAVIGATOR reads the instructions and guides the driver.
# - You will SWITCH seats and computers after every task!
# -------------------------------------------


# -------------------------------------------
# Task 1: The Personalised Welcomer
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: The Personalised Welcomer\n"
    + "-------------------------------------------")

# CONCEPT: .strip() removes "whitespace" (extra spaces) from text.
# Example: name = "  Alice  ".strip() -> Result: "Alice"

# TODO:
# 1. Ask the user for their first name and their surname separately.
# 2. Use .strip() on both to ensure there are no accidental spaces.
# 3. Ask for their birth year and calculate their approximate age (2026 - birth_year).
# 4. Print a message: "Hello [FIRST NAME] [SURNAME]! You are roughly [AGE] years old."
#    (Hint: Ensure the names are printed in ALL CAPS using a string method).

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 1"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: The Ticket Office (Logic)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer. Get the latest code!
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: The Ticket Office\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user what day of the week it is.
# 2. Use .lower() to ensure "Monday" and "monday" both work.
# 3. Write logic to determine the ticket price:
#    - IF it is "wednesday", print "Mid-week discount! Tickets are £5."
#    - ELIF it is "saturday" OR "sunday", print "Weekend prices: £10."
#    - ELSE print "Standard price: £8."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 2"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: The "Even Only" Table (Loops)
# -------------------------------------------
# INSTRUCTION: Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: The Even Only Table\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a number.
# 2. Use a 'for' loop to print the multiplication table for that number (1 to 10).
# 3. CHALLENGE: Only print the result if the answer is an EVEN number.
#    (Hint: You will need an 'if' statement inside your 'for' loop).
#
# EXPECTED OUTPUT (if number is 3):
# 3 x 2 = 6
# 3 x 4 = 12...

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_review.py
#    git commit -m "Completed Task 3"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Secure Username Pro
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "Extension 1: The Secure Username Pro\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for their favourite city and a 4-digit year.
# 2. Create a username by combining the first 3 letters of the city 
#    with the last 2 digits of the year.
#    (Hint: Use slicing like city[0:3] and year[2:4]).
# 3. Print the result in lowercase.

# Write your code below:


# Extension 2: The Average Master
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: The Average Master\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user how many scores they want to average.
# 2. Use a 'while' loop to ask for that many scores one by one.
# 3. Keep a "running total" variable.
# 4. After the loop, calculate the average and print it.
#    (Challenge: If the average is over 90, print "Scholarship Level!").

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_review.py
#    git commit -m "Completed extensions"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Smart Vending Machine
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Smart Vending Machine\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'balance' and set it to 20 (think of it as 20 pounds).
# 2. Create a 'while' loop that runs as long as the balance is above 0.
# 3. Inside the loop, show the user a menu:
#    - A: Crisps (£2)
#    - B: Drink (£3)
#    - C: Exit
# 4. Ask for their choice. Use .upper() to handle lowercase input.
# 5. IF they choose a snack they can afford, subtract the price from 'balance'.
# 6. IF they cannot afford it, print "Insufficient funds!".
# 7. Print their remaining balance after every purchase.

# Write your code below:


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex2_review.py
#    git commit -m "Completed all activities"
#    git push origin main
# -------------------------------------------
