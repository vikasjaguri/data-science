# 2. Write an OOP based Python program which inputs n numbers in a list from keyboard. If 8
# numbers are inputted, calculate sum of 0th and 7th element and save it in another list say
# newlist[0], sum of 1st and 6th to newlist[1], sum of 2nd and 5th to newlist[2], sum of 3rd and 4th
# to newlist[3] and so on. Remove duplicates from newlist if any by converting to set. Later
# convert it to tuple and display.

class SumList:
    def __init__(self, num_list):
        self.num_list = num_list

    def calculate_sums(self):
        new_list = []
        for i in range(len(self.num_list)):
            new_list.append(self.num_list[i] + self.num_list[-i-1])
        return list(set(new_list))

    def display(self):
        print("Tuple without duplicates: ", tuple(self.calculate_sums()))

# Input numbers
n = int(input("Enter the number of elements: "))
num_list = []
for _ in range(n):
    num = int(input("Enter a number: "))
    num_list.append(num)

print(num_list)
# Create an instance of SumList and call the methods
sum_list = SumList(num_list)
sum_list.display()