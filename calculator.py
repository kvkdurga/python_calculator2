"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:

    user_input = input("Enter your equation:")
    token = user_input.split(" ") 
    #print(token) 
 
    if(token[0] == "q"): 
        break 
    else:
        if(token[0] == 'add'):
            result = add(int(token[1]), int(token[2]))
            print(result)
        elif(token[0] == 'subtract'):
            result = subtract(int(token[1]), int(token[2]))
            print(result)
        elif(token[0] == 'multiply'):
            result = multiply(int(token[1]), int(token[2]))
            print(result)
        elif(token[0] == 'divide'):
            result = divide(int(token[1]), int(token[2]))
            print(result)
        elif(token[0] == 'square'):
            result = square(int(token[1]))
            print(result)
        elif(token[0] == 'cube'):
            result = cube(int(token[1]))
            print(result)
        elif(token[0] == 'power'):
            result = power(int(token[1]), int(token[2]))
            print(result)
        elif(token[0] == 'mod'):
            result = mod(int(token[1]), int(token[2]))
            print(result)
        else:
            break
        
        


