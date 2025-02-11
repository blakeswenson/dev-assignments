## Program: Decking Cost Calculator
## Date: 2/11/2025
## Author: Blake Swenson
## Purpose: Allow a user to calculate the cost of a deck based on the square footage and the type of decking material they choose.

price_per_square_foot = {
    'lumber': 2.35,
    'redwood': 7.75,
    'composite': 8.50,
}

print('Welcome to Decking Cost Calculator!') ## Print the title of the application first
square_footage = int(input('Enter the square footage of the deck: ')) ## Ask the user to enter the square footage of the deck

if square_footage > 0: ## Check if the user entered a valid square footage
    print('Type the type of decking material:')  ## Tell the user the types of decking material
    material_type = input('Lumber ($2.35 sq/ft), Redwood ($7.75 sq/ft), or Composite ($8.50 sq/ft): ').lower() ## Ask the user to enter the type of decking material
    if material_type not in price_per_square_foot: ## Check if the user entered a valid material type
        print('Invalid entry')
        print('Did you enter lumber, redwood, or composite? Please, try again.') ## Print an error message if the user entered an invalid material type
    else:
        cost = price_per_square_foot[material_type] * square_footage ## Calculate the cost of the deck
        print(f'{square_footage} square feet of {material_type} decking will cost ${cost:.2f}') ## Print the cost of the deck
        print('Thank you!') ## Print a thank you message
else:
    print('Invalid entry')
    print('Did you enter a whole number greater than zero? Please, try again.') ## Print an error message if the user entered an invalid square footage
