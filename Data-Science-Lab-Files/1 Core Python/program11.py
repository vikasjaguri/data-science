#11. Write a program to input roll number, student name, marks of physics, chemistry and maths out of 100. 
## Calculate total, percentage, calculate STATUS (pass, fail), if student score above 40 in all the 3 subjects the STATUS should be pass otherwise fail
## Calculate GRADE if STATUS is pass. Grade must be in percentage value.
## If percentage is above 70, then the GRADE must be DISTINCTION if percentage is above 60, then grade must be FIRST CLASS.
## If percentage is above 50, then GRADE must be SECOND CLASS, if percentage is above 40, then GRADE must be PASS CLASS.
rollNo = int(input("Enter roll number: "))
phy = int(input("Enter physics marks: "))
che = int(input("Enter chemistry marks: "))
mat = int(input("Enter maths marks: "))

total = phy + che + mat
percentage = total/3

if phy > 40 and che > 40 and mat > 40:
    status = "PASS"
else:
    status = "FAIL"
    
if percentage > 70:
    grade = "DISTINCTION"
elif percentage > 60:
    grade = "FIRST CLASS"
elif percentage > 50:
    grade = "SECOND CLASS"
elif percentage > 40:
    grade = "PASS CLASS"
else:
    grade = "FAIL"
print(f"Total marks: {total}")
print(f"Percentage: {percentage}%")
print(f"TStatus: {status}")
print(f"Grade: {grade}")
