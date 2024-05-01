#Question 1
data = [(12345, "Diksha","diksha@nuv.ac.in"),(45667,"Jiva","jiva@nuv.ac.in"),(16789,"Ronit","ronit@nuv.ac.in"),(69433,"Heena","heena@nuv.ac.in")]

def search_ID(stdID):
    for i in data:
        stdID = i[0]
        stdName = i[1]
        stdEmail = i[2]
        if (i[0]==id):
            print(f"ID: {stdID}, Name: {stdName}, Email: {stdEmail}")
        
def search_Name(stdName):
        for i in data:
            stdID = i[0]
            stdName = i[1]
            stdEmail = i[2]
            if (i[1]==name):
                print(f"ID: {stdID}, Name: {stdName}, Email: {stdEmail}")
                
str = input("Search by ID or Name")
if str == "ID":
    id = int(input("Enter the ID :"))
    search_ID(id)
else:
    name = input("Enter the name :")
    search_Name(name)