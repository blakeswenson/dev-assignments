play_names = {
    'Romeo and Juliet',
    'Macbeth',
    'Hamlet',
}

ticket_types = {
    'Romeo and Juliet': {
        'Orchestra': 100,
        'Mezzanine':  75,
        'Balcony':    50,
    },
    'Macbeth': {
        'Orchestra':  90,
        'Mezzanine':  70,
        'Balcony':    45,
    },
    'Hamlet': {
        'Orchestra':  80,
        'Mezzanine':  65,
        'Balcony':    40,
    },
}

play_selected = 'None'
seating_selected = 'None'
cost_per_seat = 0
qty_selected = 0

def validate_play(user_input):
    print('Hello world')
    if user_input is int and (0 < user_input <= 3):
        play_selected = play_names[user_input - 1]
    else:
        print('Invalid input')

def select_play():
    print('Hello world')

    while play_selected == 'None':
        validate_play(int(input('Select a play (1: Romeo and Juliet, 2: Macbeth, 3: Hamlet):')))

def validate_seating(user_input):
    print('Hello world')

    if user_input is int and (0 < user_input <= 3):
        seating_selected = ticket_types[play_selected][user_input - 1]
        cost_per_seat = 
        ## TODO: Check assignment of these variables with ChatGPT
    else:
        print('Invalid input')

def select_seating():
    print('Hello world')

    while seating_selected == 'None':
        validate_play(input(f'Select seating (Orchestra ${ticket_types[play_selected][0]}, Mezzanine ${ticket_types[play_selected][1]}, Balcony ${ticket_types[play_selected][2]},):'))

def validate_tickets(user_input):
    if user_input is int and user_input > 0:
        qty_selected = user_input
    else:
        print('Invalid input')

def select_tickets():
    print('Hello world')

    while qty_selected == 0:
        validate_play(int(input('Enter number of tickets:')))

def display_booking_summary():
    print('Hello world')

def book_theater_tickets():
    print('Hello world')
    total_cost = cost_per_seat * qty_selected
    print(f'You selected {qty_selected} seats to {play_selected} for ${total_cost}! Thank you!')

if __name__ == '__main__':
    book_theater_tickets()
    select_play()
    select_seating()
    select_tickets()
    display_booking_summary()
