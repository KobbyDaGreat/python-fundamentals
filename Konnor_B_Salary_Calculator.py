#This program accepts calculates Employee salary

# Pseudocode
# Create a constant for the number of employees.
# In the main function:
# Call the data_entry() to collect employee names, hours worked,
# and hourly pay rates and store them in lists.
# Call the salary_calc() and pass the hours and pay rate lists.
# salary_calc() calculates gross salary, income tax, and
# net salary and returns these lists.
#
# In data_entry function:
# Create parallel lists for employee names, hours worked,
# and pay rate.
# Use exception handling to handle errors
# Use a loop to gather input for each employee.
# Store the values in the lists.
# Return the three lists.
#
# In salary_calc function:
# Create lists for gross salary, income tax, and net salary.
# Get the gross salary, income tax, and net salary for each employee.
# Use exception handling to handle errors
# Store each value in its list.
# Return the lists.
#
# In the display_report function:
# Print a table header.
# Loop through each employee.
# Print their information in a formatted row.
# Round all numeric values to two decimal places.


# Create a global constant to control the number of employees
NUM_OF_EMPLOYEES = 6

def main():
    # Get employee data from the user
    employee_name, hours_worked, pay_rate = data_entry()

    # Calculate gross salary, tax, and net salary
    gross_salary, income_tax, net_salary = salary_calc(hours_worked, pay_rate)

    # Display the final salary report
    display_report(employee_name, hours_worked, pay_rate, gross_salary, income_tax, net_salary)

# Define the data entry function
def data_entry():
    # Create the lists to store the employee information
    employee_name = [0] * NUM_OF_EMPLOYEES
    hours_worked = [0] * NUM_OF_EMPLOYEES
    pay_rate = [0] * NUM_OF_EMPLOYEES

    # Use exception handling to validate the input from the user
    try:
        # Use the for loop to collect the data and store in the approrpiate list using index method
        for index in range(NUM_OF_EMPLOYEES):
            employee_name[index] = str(input(f'Enter the name of employee {index + 1}: '))
            hours_worked[index] = float(input(f'Enter the hours worked for employee {index + 1}: '))
            pay_rate[index] = float(input(f'Enter the pay rate for employee {index + 1}: '))
    except Exception as err:
        print(err)
    # return the lists when the function is called    
    return employee_name, hours_worked, pay_rate

        

# Define the salary_calc function using hours worked and pay rate as arguments   
def salary_calc(hours_worked, pay_rate):
    # Create lists to hold the salary details for the number of employees
    gross_salary = [0] * NUM_OF_EMPLOYEES
    income_tax = [0] * NUM_OF_EMPLOYEES
    net_salary = [0] * NUM_OF_EMPLOYEES

    # Use exception handling to validate the users input
    try:
        # Use the for loop to collect the salary data and store in the appropriate list using the index method
        for index in range(NUM_OF_EMPLOYEES):
            gross_salary[index] = hours_worked[index] * pay_rate[index]
            # The conditional controls how the income tax is calculated
            # based on the pay rate
            if pay_rate[index] <= 20.99:
                income_tax[index] = 0.15 * gross_salary[index]
            else:
                income_tax[index] = 0.20 * gross_salary[index]
            net_salary[index] = gross_salary[index] - income_tax[index]
    except Exception as err:
        print(err)
    # return the lists when the function is called     
    return gross_salary, income_tax, net_salary

# Define the display function to display the output to the user
# Use the employee data to be displayed as arguments
def display_report(employee_name, hours_worked, pay_rate, gross_salary, income_tax, net_salary):
    # Create the table headings
    print("Employee Number\tEmployee Name\tHours Worked\tHourly Salary\tGross Pay\tIncome Tax\tNet Salary")
    print(".................................................................................................................")
    # Use a loop to display the information for each worker
    for index in range(NUM_OF_EMPLOYEES):
        print(f'{index + 1}\t\t{employee_name[index]}\t\t'
              f'{hours_worked[index]}\t\t{pay_rate[index]}\t\t'
              f'{gross_salary[index]:.2f}\t\t{income_tax[index]:.2f}\t\t'
              f'{net_salary[index]:.2f}')
    
    
    
# Call the main function
if __name__ == "__main__":
    main()
