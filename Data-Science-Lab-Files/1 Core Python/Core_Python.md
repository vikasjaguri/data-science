#1. what is 7 to the power of 4?
a = 7
b = 4
print(a**b)

#2. split the string s = "hi there sam" into a list.
c = "hi there sam"
print(c.split())

#3. give the variables: planet = "Earth", diameter = 12742. Use .format() to print the following string. "The diameter of earth is 12742 kilometers".
planet = "Earth"
diameter = 12742
statement = "The diameter of {} is {} kilometers".format(planet, diameter)
print(statement)

#4. Give the nested list, use indexing to grab the word "hello". lst = [1,2,[3,4],[5,[100,200,['hello]],23,11],1,7]
def find_string(lst):
    for i in lst:
        if type(i) == list:
            result = find_string(i)
            if result:
                return result
        elif type(i) == str:
            return i

lst = [1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
print(find_string(lst))

#5. Given the nested dictionary grab the word "hello". d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
def find_hello(d):
    target_word = d['k1'][3]['tricky'][3]['target'][3]
    return target_word

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
result = find_hello(d)
print(result)

#6. What is the main difference between a tuple and a list?

#7. Create a function that grabs the email website domain from a string in the form : **user@domain.com.
#so for example, passinf "user@domain.com" would return: domain.com.
def get_domain(email):
    user, domain = email.split('@')
    return domain

email_address = "user@domain.com"
result = get_domain(email_address)
print(result)

#8. Create a basic function that returns True if the word 'dog' is contained in the input string. Dont worry about the edge cases like a 
## punctuation being attached to the word 'dog'.
def find_dog(s):
    return "dog" in s.lower()
print(find_dog("Is there a dog here?"))

#9. Use lambda expression and the filter() function to filter out the words from a list that dont start with the letter 's'.
## For example: seq = ['soup','dog','salad','cat','great'] should be filtered down to ['soup','salad'].
seq = ['soup','dog','salad','cat','great']
result = list(filter(lambda word: word[0] == 's', seq))
print(result)

#10. You are driving a little too fast, and a police officer stops you.
## Write a function to  return one of the 3 possible results: "No ticket", "Small ticket", or "Big ticket".
## If your speed is 60 or less, the result is "No ticket".
## If your speed is between 61 and 80, the result is "Small ticket".
## If your speed is 81 or more, the result is "Big ticket".
## Unless its your birthday (encoded as a boolean value in the parameter of the function) -- on your birthday, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return "No ticket"
    elif speed <= 80:
        return "Small ticket"
    else:
        return "Big ticket"
    
print(caught_speeding(67,True))

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



#12. Write an OOP in python to input empid, name, basic salary, number of experience in years. Calculate HRA (35% of basic), DA((58% of basic), and PF(9.5% of basic).
## Also calculate bonus based on experience in years.
## If experience in years is >= 30, bonus must be 59% of basic, if experience in years is >= 23, bonus must be 51% of basic,
## if experience in years is >= 15, bonus must be 45% of basic, if experience in years is >=7, bonus must be 33% of basic.
## Calculate net salary as basic + DA + PF + HRA + bonus.
## Create a class,  constructor to create instance variables, getter-setter for each variable, calculate functions for operative variables.
## A class method/function should not contain.
## Display specific and input specific code. Such code should be added in driver part of python program.