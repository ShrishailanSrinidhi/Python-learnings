# Sorting a string
 
# initializing string
from numbers import Real


#test_string ="Today is Friday"
test_string = input("Enter the string:")
 
# printing original string
print("The original string : " + str(test_string))

#convert string into lowecase and make it an array using split function
inpM = test_string.lower()
RealI = inpM.split()
#print(RealI)

# Sorting a string
Inres = ' '.join(sorted(RealI))
res = Inres.title()
     
# print result
print("String after sorting : " + str(res))