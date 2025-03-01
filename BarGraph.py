## Name: Blake Swenson
## Date: 2/27/2025
## Application; VSCodeAssignment5
## Purpose: Display a horizontal bar graph of categorical and integer data

#1. Define variables for data entry (e.g., data_entry)
# and initialize it to an empty string,
# an empty list variable for holding data categories (e.g., data_categories),
# and an empty list variable for holding the data numbers (e.g. data_numbers).

import matplotlib.pyplot as plt

data_entry = ''
data_categories = []
data_numbers = []

#2. Prompt the user for the graph title and assign the input to the data
graph_title = input('Enter the title of the graph: ')
print('You entered:', graph_title)

#3. Prompt the user for column 1 and column 2 headers in sequence
#4. Print 

column1_header = input('Enter the column 1 header:')
print('You entered:', column1_header)

column2_header = input('Enter the column 2 header:')
print('You entered:', column2_header)

#5. Prompt the user for the data entry in the form of category, number pairs
data_entry = input('Enter a data point (-1 to stop input):')

#6. While data entry is not equal to 1 split the data_entry into two tokens and add them to the my_tokens list
 
while data_entry != '-1':
    my_tokens = data_entry.split(',')

    #assign the first token to a variable e.g., data_string
    #assign the second token to a variable e.g., data_integer
    data_string = my_tokens[0]
    data_integer = my_tokens[1]

    #print both variables
    print('Data string:', data_string)
    print('Data integer:', data_integer)
    
    data_categories.append(data_string)
    data_numbers.append(data_integer)

    #prompt for another data point
    data_entry = input('Enter a data point (-1 to stop input):')

##7. Create a bar plot by modifying instructions 

#plotting data_categories and data_numbers
x_pos = range(len(data_categories)) # creates the number of bars required
plt.barh(x_pos, data_numbers)  #creates a horizontal bar graph ploting performance versus the number of bars required
plt.yticks(x_pos, data_categories) # labels the bars with programming language names
plt.xlabel(column2_header) #label the x-axis
plt.title(graph_title) #label the graph title
plt.show() #show the graph
