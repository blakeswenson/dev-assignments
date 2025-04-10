## Project Time Tracker
## Developer: Blake Swenson
## Date: 3/13/2025
## Purpose: This application is designed to help users monitor and evaluate the time spent on key project tasks.
## By comparing the planned hours with the actual hours entered by the user on each of the project tasks, the program provides insight into project time management efficiency.
## tickets based on the selected play, seating type, and the number of tickets requested by the user.

time_goals = {
    "Research": 3,
    "Writing":  5,
    "Review":   2,
}
## Table for the company to input their hour time goals for each task

def validate_num(user_input):
    if user_input < 0:
        print('Invalid entry. Please enter a nonnegative number.')
        return False
    else:
        return True
## Return false if it is a negative number and provide feedback to try again
    
def calculate_diff(actual_time, planned_time):
    diff = actual_time - planned_time
    if diff < 0:
        print(f'Under the planned time by {-diff:.1f} hour(s)') ## Print out the absolute value for better user experience
    elif diff > 0:
        print(f'Exceeded the planned time by {diff:.1f} hour(s)')
    else:
        print(f'Met the planned time exactly')
## Determine if the actual time is less than, greater than, or exactly equal to the planned time    

def get_user_input(task_name):
    valid_input = False
    time_spent = 0
    while valid_input == False:
        time_spent = float(input(f'Time Spent on {task_name}:'))
        valid_input = validate_num(time_spent)
    return time_spent
## Get the user input for time spent on task, and valide it using the validate_num() function

def project_time_tracker():
    print('PROJECT TIME TRACKER')

    ## INITALIZATION ## 

    total_actual_time = float(0)
    total_planned_time = float(0)
    ## Set to float since partial hours are an acceptable input

    ## RESEARCH ##

    research_time = get_user_input('Research')
    calculate_diff(research_time, time_goals['Research'])
    total_actual_time += research_time
    total_planned_time += time_goals['Research']

    ## WRITING ## 

    writing_time = get_user_input('Writing')
    calculate_diff(writing_time, time_goals['Writing'])
    total_actual_time += writing_time
    total_planned_time += time_goals['Writing']

    ## REVIEW ## 

    review_time = get_user_input('Review')
    calculate_diff(review_time, time_goals['Review'])
    total_actual_time += review_time
    total_planned_time += time_goals['Review']

    ## SUMMARY ##

    print(f'Total Planned Hours: {total_planned_time}')
    print(f'Total Actual Hours: {total_actual_time}')
    if total_actual_time < total_planned_time:
        print('The project took less time than planned.')
    elif total_actual_time > total_planned_time:
        print('The project took more time than planned.')
    else:
        print('The project was completed exactly as planned.')

if __name__ == '__main__':
    project_time_tracker()
## The application is executed
