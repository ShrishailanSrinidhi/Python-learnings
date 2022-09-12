if __name__ == '__main__':
    b = ()

    n = int(input("Enter number of elements : "))
  
    # Below line read list from user using map() function 
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
  
    print("\nList is - ", a)

    b = tuple(a)
    
    print("\nTuple is - ", b)

