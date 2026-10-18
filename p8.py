def get_letter_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Calculate statistics using variable positional arguments
def calculate_statistics(*grades):
    if not grades:
        return (0, 0, 0.0, {})

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for grade in grades:
        letter = get_letter_grade(grade)
        distribution[letter] += 1

    # Return multiple values as a tuple
    return minimum, maximum, average, distribution


# Generate a flexible student report using **kwargs
def student_report(name, *grades, **details):
    minimum, maximum, average, distribution = (
        calculate_statistics(*grades)
    )

    print("\n--- Student Performance Report ---")
    print("Student Name      :", name)
    print("Subject Grades    :", grades)
    print("Additional Info   :", details)
    print("Min Grade         :", minimum)
    print("Max Grade         :", maximum)
    print("Average Grade     :", round(average, 1))
    print("Letter Distribution:", distribution)
    print("Letter Grade      :", get_letter_grade(average))
    print("-" * 38)

    return average, distribution


# Main program
if __name__ == "__main__":

    students = [
        ("Rohan", (92, 85, 78, 90, 88),
         {"attendance": 95, "projects": 88}),

        ("Aditi", (76, 82, 69, 88, 91, 84),
         {"attendance": 90, "projects": 85}),

        ("Vikram", (45, 60, 58, 72, 68),
         {"attendance": 80, "projects": 70})
    ]

    total_marks = 0
    total_subjects = 0
    class_distribution = {
        "A": 0, "B": 0, "C": 0, "D": 0, "F": 0
    }

    for name, grades, details in students:
        average, distribution = student_report(
            name, *grades, **details
        )

        total_marks += sum(grades)
        total_subjects += len(grades)

        for letter, count in distribution.items():
            class_distribution[letter] += count

    overall_average = total_marks / total_subjects

    print("\n--- Class Summary (All Students) ---")
    print("Total Students  :", len(students))
    print("Overall Average :", round(overall_average, 1))
    print("Grade Distribution:", class_distribution)
