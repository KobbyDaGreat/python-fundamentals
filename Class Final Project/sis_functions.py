# This program contains all functions for the student information
# system main program to run.


# Define the read student data function
# Set the filename as parameter

def read_student_data(filename):
# Pseudocode:
# Create an empty list to store student records.
# Open the file for reading.
# Read each line from the file.
# Remove the newline character.
# Split the line by commas into fields.
# Convert numeric fields to the proper data types.
# Store the student record in the master list.
# Handle file errors if the file cannot be opened.
# Return the list of student records.

    students = []

    try:
        data_file = open(filename, 'r')

        for line in data_file:
            line = line.rstrip('\n')
            parts = line.split(',')

            # Build one student record
            student = [
                parts[0],              # first name
                parts[1],              # last name
                parts[2],              # student ID
                parts[3],              # gender
                int(parts[4]),         # age
                int(parts[5]),         # residence status
                parts[6],              # major
                parts[7],              # minor
                float(parts[8]),       # GPA
                int(parts[9]),         # credits attempted
                int(parts[10])         # STEM designation
            ]

            students.append(student)

        data_file.close()

    except IOError:
        print('Error: The file could not be opened.')

    return students


# Define the get residence label function
# Set residence status as parameter

def get_residence_label(residence_status):
#Pseudocode:
# Use the if-else conditional to check whether the student is
# in-state or out-of-state.
# return the result

    if residence_status == 1:
        return "In-State"
    else:
        return "Out-of-State"


# Define the get stem label function
# Set stem staus as parameter

def get_stem_label(stem_status):
# Pseudocode:
# Use the if-else conditional to check if the course of study is
# stem or non-stem
# return the result

    if stem_status == 1:
        return "STEM"
    else:
        return "Non-STEM"


# Define the get academic standing function
# Set gpa as parameter

def get_academic_standing(gpa):
# Pseudocode:
# Use the if conditional to check for students academic standing
# If GPA is 3.75 or higher, return Dean's List.
# Else if GPA is 3.50 to 3.74, return Honor's List.
# Else if GPA is 2.00 to 3.49, return Normal Academic Standing.
# Else return On Probation.


    if gpa >= 3.75:
        return "Dean's List"
    elif gpa >= 3.50:
        return "Honor's List"
    elif gpa >= 2.00:
        return "Normal Academic Standing"
    else:
        return "On Probation"


# Define the get class status function
# Set credits as parameter

def get_class_status(credits):
#Pseudocode:
# Use the if conditional to check for student's class status
# If credits are between 0 and 30, return Freshman.
# Else if credits are between 31 and 60, return Sophomore.
# Else if credits are between 61 and 90, return Junior.
# Else return Senior.

    if credits <= 30:
        return 'Freshman'
    elif credits <= 60:
        return 'Sophomore'
    elif credits <= 90:
        return 'Junior'
    else:
        return 'Senior'


# Define the get cost per credit function
# Set residence status and stem status as parameters

def get_cost_per_credit(residence_status, stem_status):
# Pseudocode:
# Use the if conditional to check for student's class status
# Use the residence status as parameters
# Determine the base tuition and fees by residence status.
# If the student is STEM, add the STEM fee.
# Return the total cost per credit.


    if residence_status == 1:
        cost = 325
    else:
        cost = 650

    if stem_status == 1:
        cost += 25

    return cost


# Define the calculate paid tuition function
# Set residence status, stem status and credits completed as parameters

def calculate_paid_tuition(residence_status, stem_status, credits_completed):
# Pseudocode:
# Find the student's cost per credit. 
# Multiply by completed credits.
# Return the tuition paid so far.

    cost_per_credit = get_cost_per_credit(residence_status, stem_status)
    return cost_per_credit * credits_completed


# Define the calculate remaining credits function
# Set credits completed as parameter

def calculate_remaining_credits(credits_completed):
# Pseudocode:
# Subtract completed credits from 120.
# If the result is less than 0, return 0.
# Return remaining credits.

    remaining = 120 - credits_completed

    if remaining < 0:
        remaining = 0

    return remaining


# Define the calculate remaining tuition function
# Set residence status, stem status and credits completed as parameters

def calculate_remaining_tuition(residence_status, stem_status, credits_completed):
# Pseudocode:
# Find the remaining number of credits.
# Find the cost per credit.
# Multiply remaining credits by cost per credit.
# Return the remaining tuition.

    remaining_credits = calculate_remaining_credits(credits_completed)
    cost_per_credit = get_cost_per_credit(residence_status, stem_status)
    return remaining_credits * cost_per_credit


# Define report all students function
# Set students as parameter

def report_all_students(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student in the list.
# Print all original student fields in tabular format.

    print("1: ALL STUDENTS")
    print('-' * 140)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"Gender":<8}{"Age":<6}'
          f'{"Residence":<15}{"Major":<24}{"Minor":<24}{"GPA":<8}{"Credits":<10}{"STEM":<10}')
    print('-' * 140)

    for student in students:
        residence = get_residence_label(student[5])
        stem = get_stem_label(student[10])

        print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{student[3]:<8}{student[4]:<6}'
              f'{residence:<15}{student[6]:<24}{student[7]:<24}{student[8]:<8.2f}{student[9]:<10}{stem:<10}')

    print()


# Define the report academic standing function
# Set students as parameter

def report_academic_standing(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student.
# Determine the student's academic standing from GPA.
# Print the student ID, name, GPA, and academic standing.

    print("2: ACADEMIC STANDING OF ALL STUDENTS")
    print('-' * 80)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"GPA":<10}{"Standing":<25}')
    print('-' * 80)

    for student in students:
        standing = get_academic_standing(student[8])

        print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{student[8]:<10.2f}{standing:<25}')

    print()


# Define the report stem students function
# Set students as parameter

def report_stem_students(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student.
# If the student is STEM, print the student ID, name, major, and minor.

    print("3: STEM STUDENTS MAJOR AND MINOR")
    print('-' * 80)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"Major":<20}{"Minor":<20}')
    print('-' * 80)

    for student in students:
        if student[10] == 1:
            print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{student[6]:<20}{student[7]:<20}')

    print()


# Define the report non stem students function
# Set students as parameter

def report_non_stem_students(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student.
# If the student is non-STEM, print the student ID, name, major, and minor.

    print("4: NON-STEM STUDENTS MAJOR AND MINOR")
    print('-' * 80)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"Major":<20}{"Minor":<20}')
    print('-' * 80)

    for student in students:
        if student[10] == 0:
            print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{student[6]:<20}{student[7]:<20}')

    print()


# Define the report tuition progress function
# Set students as parameter

def report_tuition_progress(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student.
# Determine residence label and STEM label.
# Calculate remaining credits.
# Calculate tuition paid so far.
# Calculate tuition left to complete the degree.
# Display the results in table format.

    print("5: STUDENT TUITION INFORMATION")
    print('-' * 120)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"Residence":<15}{"STEM":<10}'
          f'{"Completed":<12}{"Remaining":<12}{"Paid So Far":<15}{"Still Owed":<15}')
    print('-' * 120)

    for student in students:
        residence = get_residence_label(student[5])
        stem = get_stem_label(student[10])
        completed = student[9]
        remaining = calculate_remaining_credits(completed)
        paid = calculate_paid_tuition(student[5], student[10], completed)
        owed = calculate_remaining_tuition(student[5], student[10], completed)

        print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{residence:<15}{stem:<10}'
              f'{completed:<12}{remaining:<12}${paid:<14,.2f}${owed:<14,.2f}')

    print()
    

# Define the report class status function
# Set students as parameter

def report_class_status(students):
# Pseudocode:
# Display the report title and headings.
# Loop through each student.
# Determine class status from credits.
# Print student ID, name, credits, and class status.

    print("6: CLASS STATUS REPORT")
    print('-' * 90)
    print(f'{"ID":<10}{"First Name":<15}{"Last Name":<15}{"Credits":<10}{"Class Status":<20}')
    print('-' * 90)

    for student in students:
        class_status = get_class_status(student[9])

        print(f'{student[2]:<10}{student[0]:<15}{student[1]:<15}{student[9]:<10}{class_status:<20}')

    print()
    

# Define the report gpa summary function
# Set students as parameter

def report_gpa_summary(students):
# Pseudocode:
# Set counters for total_gpa, dean_count, honor_count, normal_count and probation_count and set their totals to zero.
# Loop through all students.
# Add each GPA to the total GPA.
# Count Dean's List, Honor's List, Normal Standing, and Probation students.
# Calculate the average GPA.
# Print a summary report.

    total_gpa = 0.0
    dean_count = 0
    honor_count = 0
    normal_count = 0
    probation_count = 0

    for student in students:
        gpa = student[8]
        total_gpa += gpa

        if gpa >= 3.75:
            dean_count += 1
        elif gpa >= 3.50:
            honor_count += 1
        elif gpa >= 2.00:
            normal_count += 1
        else:
            probation_count += 1

    average_gpa = total_gpa / len(students)

    print("7: GPA SUMMARY REPORT")
    print('-' * 40)
    print(f'Total Students: {len(students)}')
    print(f'Average GPA: {average_gpa:.2f}')
    print(f'Dean\'s List Students: {dean_count}')
    print(f'Honor\'s List Students: {honor_count}')
    print(f'Normal Academic Standing: {normal_count}')
    print(f'On Probation: {probation_count}')
    print('-' * 40)
    print()


# Import the matplotlib method
import matplotlib.pyplot as plt

# Define the stem chart function
# Set students as parameter

def stem_chart(students):
# Pseudocode:
# Set STEM count to 0
# Set NON-STEM count to 0
# Loop through all students
# If student is STEM → increase STEM count
# Else → increase NON-STEM count
# Store counts in a list
# Create labels list
# Call plt.pie()
# Add title
# Show chart
    
    stem_count = 0
    non_stem_count = 0

    # Count students
    for student in students:
        if student[10] == 1:
            stem_count += 1
        else:
            non_stem_count += 1

    # Data for pie chart
    sizes = [stem_count, non_stem_count]
    labels = ['STEM', 'NON-STEM']

    # Create pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Title
    plt.title("STEM vs NON-STEM Students")

    # Show chart
    plt.show()
    
        





