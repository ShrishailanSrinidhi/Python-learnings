
"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.

Constraints
0<len(s)<=1000
"""

def swap_case(s):


    Output = '';
    # Check if letter is upper case or not. If isupper == True, it means letter is uppercase.
    # Convert to lowercase and store in Output string
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;
    

if __name__ == '__main__':
    s = input("Enter the string\n")
    result = swap_case(s)
    print(result)
