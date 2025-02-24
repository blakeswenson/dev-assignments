## Program: Scube Expedition Application
## Date: 2/24/2025 9:15 AM
## Author: Blake Swenson
## Purpose: Calculate the total due for a scube expedition based
## on the selected location, dive selected, people in group, and cost
## to practice using functions.

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

def validateLocation(location):
    if not (location == 'Australia' or location == 'Belize' or location == 'Fiji'):
        print('Please select a country from the above options. Make sure to input exactly: "Australia", "Belize", "Fiji".')
        location = 'Invalid'
    return location
## Validate location. Display error message if input is invalid

def validateNumPeople(number_of_people):
    if number_of_people <= 0:
        print('Please enter a dive team size greater than 0. Make sure to input exactly: A number greater than 0.')
        number_of_people = -1
    return number_of_people
## Validate number of people. Display error message if input is invalid

def validateDiveSelected(location, dive_selected):
    if location == 'Australia':
        if not dive_selected in australia_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Great Barrier Reef" or "Fathom Chasm".')
            dive_selected = 'Invalid'
    elif location == 'Belize':
        if not dive_selected in belize_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Great Blue Chasm" or "Rainbow Reef".')
            dive_selected = 'Invalid'
    elif location == 'Fiji':
        if not dive_selected in fiji_dives:
            print('Please select a dive type form the above options. Make sure to input exactly: "Sunken Ship" or "Tiger Shark".')
            dive_selected = 'Invalid'
    return dive_selected
## Validate dive selected. Display error message if input is invalid

def getDiveCost(location, dive_selected):
    if dive_selected != 'Invalid':
        if location == 'Australia':
            dive_cost = australia_dives[dive_selected]
        elif location == 'Belize':
            dive_cost = belize_dives[dive_selected]
        elif location == 'Fiji':
            dive_cost = fiji_dives[dive_selected]
    else:
        dive_cost = 0
    return dive_cost
## Get dive cost based on location and dive selected. No cost will be displayed later if input is invalid.

location = 'Invalid'
while location == 'Invalid':
    location = input('Enter location (Australia, Belize, Fiji):')
    location = validateLocation(location)
## User input for location.

number_of_people = -1
while number_of_people < 0:
    number_of_people = int(input('Enter number of people in  dive team):'))
    number_of_people = validateNumPeople(number_of_people)
## User input for number of people.

dive_selected = 'Invalid'
dive_cost = 0
while dive_selected == 'Invalid':
    if location == 'Australia':
        dive_selected = input('Enter dive selected (Great Barrier Reef [$350], Fathom Chasm [$250]):')
    elif location == 'Belize':
        dive_selected = input('Enter dive selected (Great Blue Chasm [$175], Rainbow Reef [$150]):')
    elif location == 'Fiji':
        dive_selected = input('Enter dive selected (Sunken Ship [$280], Tiger Shark [$225]):')
    dive_selected = validateDiveSelected(location, dive_selected)
    dive_cost = getDiveCost(location, dive_selected)
## User input for dive selected.

total_due = number_of_people * dive_cost
print(f'You have selected {dive_selected} in {location} for {number_of_people} people at a total cost of ${total_due}. Thank you!')
## Calculate total due and display message
