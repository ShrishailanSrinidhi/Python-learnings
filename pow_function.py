"""
Task
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains , the second line contains , and the third line contains .

Constraints

1<=a<=10
1<=b<=10
2<=m<=1000
"""
import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    def power(a,b):
            if 1<=a<=10 and 1<=b<=10:
                print(pow(a,b))
            else:
                print("a and b should be in range 1 to 10")

    def modulo(a,b,m):
            if 1<=a<=10 and 1<=b<=10 and 2<=m<=1000:
                print(pow(a,b,m))
            else:
                print("a or b or m is out of range. a and b should be in range 1 to 10 and m between 2 to 1000")
    
    power(a,b)
    modulo(a,b,m)

    
