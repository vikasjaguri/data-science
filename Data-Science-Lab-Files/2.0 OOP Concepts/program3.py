# 3. Write an OOP program to perform addition, base and power, concatenation, max, min of two
# numbers stored in two different objects created from same class.
# n1=MyNumber(2)
# n2=MyNumber()
# n2.setNum(5)
# n3=n1.add(n2)
# print("Addition is ",n3.getNum()) #7
# n3=n1.raisedTo(n2)
# print(n1.getNum()," raised to ",n2.getNum()," is ",n3.getNum()) #32
# n3=n1.concat(n2)
# print("Concat answer is ",n3.getNum()) #25
# n3=n1.max(n2)
# print("Max is ",n3.getNum())

class MyNumber:
    def __init__(self, n1=None,n2=None ):
        self.n1 = int(input())
        
# Function to calculate.
    def add(self, a, b):
        return a + b

    def raisedTo(self, a, b):
        return a ** b

    def concat(self, a, b):
        return int(str(a) + str(b))

    def max(self, a, b):
        return max(a, b)

    def min(self, a, b):
        return min(a, b)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
num = MyNumber()

print(num.add(n1, n2))
print(num.raisedTo(n1, n2))
print(num.concat(n1, n2))
print(num.max(n1, n2))
print(num.min(n1, n2))