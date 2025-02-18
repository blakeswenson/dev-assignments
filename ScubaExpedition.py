## Program: Scube Expedition Application 🤿
## Date: 2/20/2025
## Author: Blake Swenson
## Purpose: Calculate the total due for a scube expeditin based
## on the selected location, dive selected, people in group, total due

## TODO: Program works, add comments and add behavior for invalid inputs included in assignment
## TODO: HERE BE DRAGONS! This code is sensitive to whitespace

print('Welcome to Scube Expedition Application!')

australia_dives = {
    'Great Barrier Reef': 350,
    'Fathom Chasm': 250
}

belize_dives = {
    'Great Blue Chasm': 175,
    'Rainbow Reef': 150
}

fiji_dives = {
    'Sunken Ship': 280,
    'Tiger Shark': 225
}

location = 'Invalid'
while location == 'Invalid':
    location = input('Enter location (Australia, Belize, Fiji):')
    if not (location == 'Australia' or location == 'Belize' or location == 'Fiji'):
        location = 'Invalid'

number_of_people = int(input('Enter number of people in  dive team):'))

dive_selected = 'Invalid'
dive_cost = 0
while dive_selected == 'Invalid':
    print(location)
    if location == 'Australia':
        dive_selected = input('Enter dive selected (Great Barrier Reef [$350], Fathom Chasm [$250]):')
        if not dive_selected in australia_dives:
            dive_selected = 'Invalid'
        else:
            dive_cost = australia_dives[dive_selected]
    elif location == 'Belize':
        dive_selected = input('Enter dive selected (Great Blue Chasm [$175], Rainbow Reef [$150]):')
        if not dive_selected in belize_dives:
            dive_selected = 'Invalid'
        else:
            dive_cost = belize_dives[dive_selected]
    elif location == 'Fiji':
        dive_selected = input('Enter dive selected (Sunken Ship [$280], Tiger Shark [$225]):')
        if not dive_selected in fiji_dives:
            dive_selected = 'Invalid'
        else:
            dive_cost = fiji_dives[dive_selected]

total_due = number_of_people * dive_cost
print(f'Total due for {location} {dive_selected} with {number_of_people}: ${total_due}')
