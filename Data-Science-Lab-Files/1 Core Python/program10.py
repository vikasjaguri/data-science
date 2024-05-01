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
