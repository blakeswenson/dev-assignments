## Program: Weight Loss Calculator
## Date: 2/18/2025
## Author: Blake Swenson
## Purpose: Calculate the average weight loss of a team of people

print('Welcome to Weight Loss Calculator!')

team_size = int(input('Input number of team members:')) # User input for team size
total_weight_loss = 0 ## Initialize total weight loss to 0

for i in range(team_size): # Loop to get weight loss for each team member
    weight_loss = -1
    while weight_loss < 0: ## Loop to check for negative input
        weight_loss = int(input(f'Enter team member #{i + 1} weight loss:')) ## User input for weight loss
        if weight_loss < 0: ## Check for negative input
            print('Invalid input. Please enter a positive number.') 
        else:
           total_weight_loss += weight_loss ## Add weight loss to total

average_weight_loss = total_weight_loss / team_size ## Calculate average weight loss
print(f'Average weight loss: {average_weight_loss:.2f} lbs.')
