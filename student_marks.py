# Create the dictionary
student_marks = {
    "Ekjati": 95,
    "Bulaaki Masaan": 90,
    "Sur Sundari": 98,
    "Kaluaa Veer": 92,
    "Kaal Bhairav": 88
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve marks or show error
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
