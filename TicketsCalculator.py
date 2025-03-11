play_names = {  ## Plays
    0: 'Romeo and Juliet',
    1: 'Macbeth',
    2: 'Hamlet',
}

seat_types = {  ## Seating levels
    0: 'Orchestra',
    1: 'Mezzanine',
    2: 'Balcony',
}

ticket_types_1 = {  ## Romeo and Juliet seating costs
    0: 100,  ## Orchestra
    1: 75,   ## Mezzanine
    2: 50,   ## Balcony
}
ticket_types_2 = {  ## Macbeth seating costs
    0: 90,   ## Orchestra
    1: 70,   ## Mezzanine
    2: 45,   ## Balcony
}
ticket_types_3 = {  ## Hamlet seating costs
    0: 80,   ## Orchestra
    1: 65,   ## Mezzanine
    2: 40,   ## Balcony
}

## Define global variables
play_selected = 'None'
seat_type = 'None'
cost_per_seat = 0
ticket_quantity = 0
total_cost = 0

def validate_play(user_input): ## Validate play selection
    global play_selected
    if user_input > 0 and user_input <= 3: ## Making sure user input is not too high or low, and then choosing the play and assigning relevant variables
        play_selected = play_names[user_input - 1]
        print(play_selected)
    else:
        print('Invalid input')

def select_play(): ## Select play
    global play_selected
    while play_selected == 'None':
        validate_play(int(input('Select a play (1: Romeo and Juliet, 2: Macbeth, 3: Hamlet):'))) ## User inputs the play, keep repeating if invalid

def validate_seating(user_input): ## Validate seating selection
    global play_selected
    global seat_type
    global cost_per_seat
    global total_cost
    print(user_input)
    if user_input > 0 and user_input <= 3: ## Making sure user input is not too high or low, and then finding cost per seat from relevant table
        seat_type = seat_types[user_input - 1]
        if play_selected == 'Romeo and Juliet':
            cost_per_seat = ticket_types_1[user_input - 1]
        elif play_selected == 'Macbeth':
            cost_per_seat = ticket_types_2[user_input - 1]
        elif play_selected == 'Hamlet':
            cost_per_seat = ticket_types_3[user_input - 1]
    else:
        print('Invalid input')

def select_seating(): ## Select seating
    global play_selected
    global seat_type
    while seat_type == 'None': ## Choosing the seat with user input, keep repeating if invalid 
        if play_selected == 'Romeo and Juliet':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_1[0]}, 2: Mezzanine ${ticket_types_1[1]}, 3: Balcony ${ticket_types_1[2]}):')))
        elif play_selected == 'Macbeth':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_2[0]}, 2: Mezzanine ${ticket_types_2[1]}, 3: Balcony ${ticket_types_2[2]}):')))
        elif play_selected == 'Hamlet':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_3[0]}, 2: Mezzanine ${ticket_types_3[1]}, 3: Balcony ${ticket_types_3[2]}):')))


def validate_tickets(user_input): ## Validate ticket quantity
    global ticket_quantity
    if user_input > 0: ## Make sure the user is not buying negative or zero tickets
        ticket_quantity = user_input
    else:
        print('Invalid input')

def select_tickets(): ## Select ticket quantity
    global ticket_quantity
    while ticket_quantity == 0: ## User inputs the number of tickets, keep repeating if invalid
        validate_tickets(int(input('Enter number of tickets:')))

def calculate_total_cost(): ## Calculate total cost
    global cost_per_seat
    global ticket_quantity
    global total_cost
    print(cost_per_seat)
    print(ticket_quantity)
    total_cost = cost_per_seat * ticket_quantity ## Calculate total cost by taking number of seats and the cost per seat

def display_booking_summary(): ## Display booking summary
    global play_selected
    global seat_type
    global cost_per_seat
    global ticket_quantity
    global total_cost
    print(f'You selected {ticket_quantity} seats in {seat_type} level (${cost_per_seat} each) to {play_selected} for ${total_cost}! Thank you!') ## Print summary output

def book_theater_tickets(): ## Primary function of the program with all other functions
    select_play()
    select_seating()
    select_tickets()
    calculate_total_cost()
    display_booking_summary()

if __name__ == '__main__': ## Main function 
    book_theater_tickets()
