################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

# function for determining letter grade based on average scores
def getLetterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    elif grade >= 50:
        return 'E'
    else:
        return 'F'
   

################ Main Program ################

# Application Loop

# create empty dictionary and empty option selection
students = {
  
}
option = ""

while(option != 6):
    # Prompt the user to select an option
    print()
    displayMenu()
    print()
    option = input("Select an Option: ")
    print()  
        
    # option 1: add a student
    if option == "1":
           name = input("Enter student name: ")
           students[name] = []   
           print(f"{name} has been added!")
          
    # option 2: remove a student
    elif option == "2":
        name = input("Enter student name: ")
        if name in students:
           del students[name]
           print(f"{name} has been removed!")
        else:
            print(f"{name} is not in our records!")

    # option 3: add a grade to a student report card
    elif option == "3":
        name = input("Enter a student name: ")
        if name in students:
            grade = getNumberGradeFromUser()
            students[name].append(grade)
            print(f"Added {grade} to {name}'s grades!")
        else:
            print(f"{name} is not in our records!")

  # list all grades for a student
    elif option == "4":
        name = input("Enter student name: ")
        if name in students:
           grades = students[name]
           print(f"{name}'s grades: ")
           for grade in grades:
              print(grade)    
        else:
            print(f"{name} is not in our records!")
              
  # display average grade for a student
    elif option == "5":
       name = input("Enter student name: ")
       if name in students:
           grades = students[name]
           numGrades = len(grades)
           # check if there are any grades entered for the student. If so, do the math to get average grade
           if numGrades > 0:
               gradeSum = sum(grades)
               gradeAvg = gradeSum / numGrades
               letterGrade = getLetterGrade(gradeAvg)
               print(f"{name}'s average letter grade is {letterGrade}")
           else:
               print(f"{name} has no grades in our records!")

       else:
           print(f"{name} is not in our records!")

  # program should end when 6 is entered