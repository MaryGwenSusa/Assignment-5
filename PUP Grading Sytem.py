def header():
    print(f"Polytechnic University of the Philippines (PUP) Grading System")

if gradeP >= 97 and gradeP <= 100:
        print("Grade/Mark: 1.00")
        print(f"Description: {status[1]}")
elif gradeP >= 94 and gradeP <= 96:
    print("Grade/Mark: 1.25")
    print(f"Description: {status[1]}")
elif gradeP >= 91 and gradeP <= 93:
    print("Grade/Mark: 1.5")
    print(f"Description: {status[2]}")
elif gradeP >= 88 and gradeP <= 90:
    print("Grade/Mark: 1.75")
    print(f"Description: {status[2]}")