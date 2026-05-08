# This is a School Information System that provides student information.

# Pseudocode
# Define the main function to control the program.
# Read the student information system functions file
# Define the display menu function to welcome message and
# display options to the user.
# Use a while loop to match user's choice to report function.

# Import the student information systems functions from the library file
import sis_functions

def main():

    # Load the student data
    students = sis_functions.read_student_data("Data_Final_Project.txt")

    # This counter countrols the loop
    user_choice = 0
    
    # Loop until user exits the program and validates input.
    while user_choice != 9:
        user_choice = display_menu()

        if user_choice == 1:
            sis_functions.report_all_students(students)
        elif user_choice == 2:
            sis_functions.report_academic_standing(students)
        elif user_choice == 3:
            sis_functions.report_stem_students(students)
        elif user_choice == 4:
            sis_functions.report_non_stem_students(students)
        elif user_choice == 5:
            sis_functions.report_tuition_progress(students)
        elif user_choice == 6:
            sis_functions.report_class_status(students)
        elif user_choice == 7:
            sis_functions.report_gpa_summary(students)
        elif user_choice == 8:
            sis_functions.stem_chart(students)
        elif user_choice == 9:
            print("Goodbye!")
            print("Closing the program....")
        else:
            print("Invalid choice!!! Try again.")
            print()



# Define the display menu function

def display_menu():
    # Display the welcome screen and get the user choice
    
    print("=====STUDENT INFORMATION=====")
    print("*************************************")
    print()
    print("Welcome to the students information systems.")
    print("Please enter the number that corresponds")
    print("with the option you want to execute.")
    print()
    print("************************************************")
    print()
    print("1 = Display All Student Information")
    print("2 = Display All Student Academic Standing")
    print("3 = Display Major & Minor of all STEM Students")
    print("4 = Display Major & Minor of all Non-STEM Students")
    print("5 = Display Detailed Student Tuition Information")
    print("6 = Display Student Class Status")
    print("7 = Display Student GPA Summary")
    print("8 = Display Student STEM classification chart")
    print("9 = Exit the program")
    user_choice= int(input("Please select an option from the above menu: "))
    print()
    return user_choice




if __name__ == "__main__":
    main()
