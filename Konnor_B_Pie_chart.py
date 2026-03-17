# This program reads data from a file and visualizes
# the data on a pie chart.

# Pseudocode
# Import the matplotlib module.
# Define the main function that will control the program.
# Create the empty lists to hold the contents of the file to be read.
# Use try/except to handle and display any errors in the program.
# Open the file and read the contents.
# Populate the amounts and labels lists with the details from the espenses file.
# Close the file.
# Name the pie chart, plot it, and display.

# Import the matplotlib method
import matplotlib.pyplot as plt
        
# Define the main function to control the program
def main():
    # Create a list of amounts
    amounts = []

    # Create a list of labels for the slices
    slice_labels = []

    # Use exception handling to handle and show errors
    try:
        

        # Open the expenses file for reading
        expenses_file = open('expenses.txt', 'r')

        # Read the labels name on the file into the slice labels list
        for line in expenses_file:
            parts = line.split()

            # store the labels in the slice label list
            slice_labels.append(parts[0])

            # store the amounts in the amounts list
            amounts.append(float(parts[1]))

        # close the expenses file
        expenses_file.close()
        

        # Create a pie chart from the values
        plt.pie(amounts, labels= slice_labels, colors=('r', 'g', 'b', 'y', 'k', 'c'))

        # Add a title to the pie chart
        plt.title("Monthly Expenses")

        # Display the pie chart
        plt.show()

    # display the exception error
    except Exception as err:
        print(err)


        

# Call the main function to execute the program
if __name__=="__main__":
    main()
    
    






