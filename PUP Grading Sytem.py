def header():
    print(f"Polytechnic University of the Philippines (PUP) Grading System")

def condition(*status):
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
    elif gradeP >= 85 and gradeP <= 87:
        print("Grade/Mark: 2.00")
        print(f"Description: {status[3]}")
    elif gradeP >= 82 and gradeP <= 84:
        print("Grade/Mark: 2.25")
        print(f"Description: {status[3]}")
    elif gradeP >= 79 and gradeP <= 81:
        print("Grade/Mark: 2.5")
        print(f"Description: {status[4]}")
    elif gradeP >= 76 and gradeP <= 78:
        print("Grade/Mark: 2.75")
        print(f"Description: {status[4]}")
    elif gradeP == 75:
        print("Grade/Mark: 3.00")
        print(f"Description: {status[5]}")
    elif gradeP >= 65 and gradeP <= 74:
        print("Grade/Mark: 5.00")
        print(f"Description: {status[6]}")
    else:
        print("Grade/Mark: INC./W/D")
        print(f"Description: {status[7]}")