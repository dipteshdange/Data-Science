# grade_calculator.py

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! You're a star! "
    elif marks >= 80:
        return "B", "Very Good! Keep it up! "
    elif marks >= 70:
        return "C", "Good job! You can do even better! "
    elif marks >= 60:
        return "D", "Keep trying! Practice more! "
    else:
        return "F", "Don't give up! Work harder and you'll improve! "


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("Student Grade Calculator\n")

    name = input("Enter student name: ").strip().title()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n RESULT FOR", name.upper() + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run the program
if __name__ == "__main__":
    main()
