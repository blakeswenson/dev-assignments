play_names = [
    'Romeo and Juliet',
    'Macbeth',
    'Hamlet',
]

seat_types = [
    'Orchestra',
    'Mezzanine',
    'Balcony',
]

ticket_types_1 = [ ## Romeo and Juliet
    100, ## Orchestra
    75, ## Mezzanine
    50, ## Balcony
]
ticket_types_2 = [ ## Macbeth
    90, ## Orchestra
    75, ## Mezzanine
    45, ## Balcony
]
ticket_types_3 = [ ## Hamlet
    80, ## Orchestra
    65, ## Mezzanine
    40, ## Balcony
]

play_selected = 'None'
seat_type = 'None'
cost_per_seat = 0
ticket_quantity = 0
total_cost = 0

def validate_play(user_input):
    global play_selected
    if user_input > 0 and user_input <= 3:
        play_selected = play_names[user_input - 1]
        print(play_selected)
    else:
        print('Invalid input')

def select_play():
    global play_selected
    while play_selected == 'None':
        validate_play(int(input('Select a play (1: Romeo and Juliet, 2: Macbeth, 3: Hamlet):')))

def validate_seating(user_input):
    global play_selected
    global seat_type
    global cost_per_seat
    global total_cost
    print(user_input)
    if user_input > 0 and user_input <= 3:
        seat_type = seat_types[user_input - 1]
        if play_selected == 'Romeo and Juliet':
            cost_per_seat = ticket_types_1[user_input - 1]
        elif play_selected == 'Macbeth':
            cost_per_seat = ticket_types_2[user_input - 1]
        elif play_selected == 'Hamlet':
            cost_per_seat = ticket_types_3[user_input - 1]
    else:
        print('Invalid input')

def select_seating():
    global play_selected
    global seat_type
    while seat_type == 'None':
        if play_selected == 'Romeo and Juliet':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_1[0]}, 2: Mezzanine ${ticket_types_1[1]}, 3: Balcony ${ticket_types_1[2]},):')))
        elif play_selected == 'Macbeth':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_2[0]}, 2: Mezzanine ${ticket_types_2[1]}, 3: Balcony ${ticket_types_2[2]},):')))
        elif play_selected == 'Hamlet':
            validate_seating(int(input(f'Select seating (1: Orchestra ${ticket_types_3[0]}, 2: Mezzanine ${ticket_types_3[1]}, 3: Balcony ${ticket_types_3[2]},):')))


def validate_tickets(user_input):
    global ticket_quantity
    if user_input > 0:
        ticket_quantity = user_input
    else:
        print('Invalid input')

def select_tickets():
    global ticket_quantity
    while ticket_quantity == 0:
        validate_tickets(int(input('Enter number of tickets:')))

def calculate_total_cost():
    global cost_per_seat
    global ticket_quantity
    global total_cost
    print(cost_per_seat)
    print(ticket_quantity)
    total_cost = cost_per_seat * ticket_quantity

def display_booking_summary():
    global play_selected
    global seat_type
    global ticket_quantity
    global total_cost
    print(f'You selected {ticket_quantity} seats in {seat_type} level to {play_selected} for ${total_cost}! Thank you!')

if __name__ == '__main__':
    select_play()
    select_seating()
    select_tickets()
    calculate_total_cost()
    display_booking_summary()
