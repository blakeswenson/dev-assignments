## Program: Scube Expedition Application 🤿
## Date: 2/20/2025
## Author: Blake Swenson
## Purpose: Calculate the total due for a scube expeditin based
## on the selected location, dive selected, people in group, total due

print('Welcome to Scuba Expedition Application!')

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
## Dictionaries for dive costs

location = 'Invalid'
while location == 'Invalid':
    location = input('Enter location (Australia, Belize, Fiji):')
    if not (location == 'Australia' or location == 'Belize' or location == 'Fiji'):
        print('Please select a country from the above options. Make sure to input exactly: "Australia", "Belize", "Fiji".')
        location = 'Invalid'
## User input for location. Display error message if input is invalid

number_of_people = -1
while number_of_people < 0:
    number_of_people = int(input('Enter number of people in  dive team):'))
    if number_of_people <= 0:
        print('Please enter a dive team size greater than 0. Make sure to input exactly: A number greater than 0.')
        number_of_people = -1
## User input for number of people. Display error message if input is invalid

dive_selected = 'Invalid'
dive_cost = 0
while dive_selected == 'Invalid':
    print(location)
    if location == 'Australia':
        dive_selected = input('Enter dive selected (Great Barrier Reef [$350], Fathom Chasm [$250]):')
        if not dive_selected in australia_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Great Barrier Reef" or "Fathom Chasm".')
            dive_selected = 'Invalid'
        else:
            dive_cost = australia_dives[dive_selected]
    elif location == 'Belize':
        dive_selected = input('Enter dive selected (Great Blue Chasm [$175], Rainbow Reef [$150]):')
        if not dive_selected in belize_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Great Blue Chasm" or "Rainbow Reef".')
            dive_selected = 'Invalid'
        else:
            dive_cost = belize_dives[dive_selected]
    elif location == 'Fiji':
        dive_selected = input('Enter dive selected (Sunken Ship [$280], Tiger Shark [$225]):')
        if not dive_selected in fiji_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Sunken Ship" or "Tiger Shark".')
            dive_selected = 'Invalid'
        else:
            dive_cost = fiji_dives[dive_selected]
## User input for dive selected. Display error message if input is invalid

total_due = number_of_people * dive_cost
print(f'You have selected {dive_selected} in {location} for {number_of_people} people at a total cost of ${total_due}. Thank you!')
## Calculate total due and display message