# Question 2
myDict = {
    "Enrollment Id" : [12345,45667,16789,69433],
    "Student name" : ["Diksha","Jiva","Ronit","Heena"],
    "Email Id" : ["diksha@nuv.ac.in","jiva@nuv.ac.in","ronit@nuv.ac.in","heena@nuv.ac.in"]
}

def searchId(num):
    for i in range(len(myDict["Enrollment Id"])):
        enrId = myDict["Enrollment Id"][i]
        stdName = myDict["Student name"][i]
        stdEmail = myDict["Email Id"][i]
        
        if(myDict["Enrollment Id"][i] == id):
            print(f"{enrId:<7}{stdName:<12}{stdEmail:25}")

id = int(input("Enter the ID: "))
searchId(id)