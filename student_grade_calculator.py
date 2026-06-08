print("******** STUDENT GRADE CALCULATOR ********")

name = input("Enter your name: ")
maths = int(input("Enter Maths marks (0-100): "))
phy = int(input("Enter Physics marks (0-100): "))
chem = int(input("Enter Chemistry marks (0-100): "))
total = maths + phy + chem
average = total / 3
highest = max(maths, phy, chem)
lowest = min(maths, phy, chem)
if (maths < 0 or maths > 100) or (phy < 0 or phy > 100) or (chem < 0 or chem > 100):
    print("INVALID MARKS! Enter Marks Between 0 and 100")

else:
    print("******** REPORT ********")
    print(f"Name: {name}")
    print(f"Total Marks: {total}/300")
    print(f"Average: {round(average, 2)}")
    print(f"Highest Subject Score: {highest}")
    print(f"Lowest Subject Score: {lowest}")

    if average < 40:
        print("Grade: FAIL")
        print("You need improvement!")
    elif average < 60:
        print("Grade: D")
    elif average < 75:
        print("Grade: C")
    elif average < 90:
        print("Grade: B")
    else:
        print("Grade: A")