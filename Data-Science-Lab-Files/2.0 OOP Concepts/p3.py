class NumberOperations:
    def __init__(self, num):
        self.num = num

    def addition(self, other):
        # Addition method to add the current object's number with another object's number
        if isinstance(other, NumberOperations):
            return self.num + other.num
        else:
            raise ValueError("Invalid type for addition. Must be an instance of NumberOperations.")

    def power(self, exponent):
        # Power method to calculate the current object's number raised to the given exponent
        return self.num ** exponent

    def concatenate(self, other):
        # Concatenation method to concatenate the integer representations of two numbers as strings
        if isinstance(other, NumberOperations):
            return str(int(self.num)) + str(int(other.num))
        else:
            raise ValueError("Invalid type for concatenation. Must be an instance of NumberOperations.")

    def maximum(self, other):
        # Maximum method to find the maximum of the current object's number and another object's number
        if isinstance(other, NumberOperations):
            return max(self.num, other.num)
        else:
            raise ValueError("Invalid type for finding maximum. Must be an instance of NumberOperations.")

    def minimum(self, other):
        # Minimum method to find the minimum of the current object's number and another object's number
        if isinstance(other, NumberOperations):
            return min(self.num, other.num)
        else:
            raise ValueError("Invalid type for finding minimum. Must be an instance of NumberOperations.")

if __name__ == "__main__":
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Create two objects from the NumberOperations class
    obj1 = NumberOperations(num1)
    obj2 = NumberOperations(num2)

    # Perform operations and display results
    print(f"Addition: {obj1.addition(obj2)}")
    exponent = float(input("Enter the exponent for power operation: "))
    print(f"Power of obj1: {obj1.power(exponent)}")
    print(f"Power of obj2: {obj2.power(exponent)}")
    print(f"Concatenation: {obj1.concatenate(obj2)}")
    print(f"Maximum: {obj1.maximum(obj2)}")
    print(f"Minimum: {obj1.minimum(obj2)}")
