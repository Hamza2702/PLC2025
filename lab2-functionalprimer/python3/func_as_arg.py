def listFunc(a, b):
    return [i for i in range(a, b + 1)] #Create list of ints from 1 to 5, Haskell equivalent [1..5]

def applicatorFunc(inpFunc, s, a, b):
    if s=='s':
        return sum(inpFunc(a, b))
    else:
        return sum(inpFunc(a, b))/(b-a+1)
    
a = input("Enter a number (a)\n")
b = input("Enter another number (b)\n")
a = int(a)
b = int(b)
c = input("'s' for sum, 'a' for average\n")
print(applicatorFunc(listFunc, c, a, b))