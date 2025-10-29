# Main program loop
while True:
    # Step 1: Get user input
    print("=" * 50)
    print("GRADE CALCULATOR")
    print("=" * 50)

    name = input("Enter your name: ")
    print(f"\nHello {name}! Please enter your marks for three subjects.")

    # Get marks for three subjects
    subject1 = float(input("Enter mark for Subject 1: "))
    subject2 = float(input("Enter mark for Subject 2: "))
    subject3 = float(input("Enter mark for Subject 3: "))

    # Step 2: Calculate the average
    average = (subject1 + subject2 + subject3) / 3

    # Step 3: Determine the grade 
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Step 4 (Bonus): Determine pass or fail status
    if average >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Student Name: {name}")
    print(f"Subject 1: {subject1}")
    print(f"Subject 2: {subject2}")
    print(f"Subject 3: {subject3}")
    print(f"Average Mark: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("=" * 50)

    # Additional feedback based on grade
    if grade == "A":
        print("Excellent work! Keep it up!")
    elif grade == "B":
        print("Great job! You're doing well!")
    elif grade == "C":
        print("Good effort! There's room for improvement.")
    elif grade == "D":
        print("You passed, but consider studying more.")
    else:
        print("Don't give up! You can improve with more practice.")
    
    # Ask if user wants to continue
    print("\n" + "=" * 50)
    continue_choice = input("Do you want to calculate another grade? (yes/no): ").lower()
    
    if continue_choice != "yes" and continue_choice != "y":
        print("\nThank you for using the Grade Calculator! Goodbye!")
        print("=" * 50)
        break
    
    print("\n")  