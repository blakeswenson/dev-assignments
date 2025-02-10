## DECKING COST CALCULATOR 

pricePerSquareFoot = {
    'lumber': 2.35,
    'redwood': 7.75,
    'composite': 8.50,
}

print('DECKING COST CALCULATOR') ## Print the title of the application first
squareFootage = int(input('Enter the square footage of the deck: ')) ## Ask the user to enter the square footage of the deck

print('Select the type of decking material:')  ## Tell the user the types of decking material
materialType = input('Lumber, Redwood, or Composite: ').lower() ## Ask the user to enter the type of decking material
if materialType not in pricePerSquareFoot: ## Check if the user entered a valid material type
    print('Invalid entry')
    print('Did you enter lumber, redwood, or composite? Please, try again.')
    exit() ## Handle invalid user selection

cost = pricePerSquareFoot[materialType] * squareFootage ## Calculate the cost of the deck
print(f'{squareFootage} square feet of {materialType} decking will cost ${cost:.2f}') ## Print the cost of the deck
