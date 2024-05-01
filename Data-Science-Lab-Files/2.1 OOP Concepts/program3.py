import pandas as pd
data = [
    (12345, "Diksha", "diksha@nuv.ac.in"),
    (45667, "Jiva", "jiva@nuv.ac.in"),
    (16789, "Ronit", "ronit@nuv.ac.in"),
    (69433, "Heena", "heena@nuv.ac.in")
]

enrollment_ID = []
student_Name = []
student_Email = []

for data_tuple in data:
    id, name, email = data_tuple
    
    enrollment_ID.append(id)
    student_Name.append(name)
    student_Email.append(email)

myDict = {
    "Enrollment Id": enrollment_ID,
    "Student name": student_Name,
    "Email Id": student_Email
}

df = pd.DataFrame(myDict)
print(myDict)
print(df)