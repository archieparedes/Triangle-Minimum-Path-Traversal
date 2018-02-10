"""
Python Intern Test
Created on Sun JAN 28 12:34:51 2018
@author: Archie Paredes
"""
def minPath(twoDLst, intLst):
    minLst = [] # Returned list
    c = 0 # index for element comparison

    for row in range(0, len(twoDLst)):
        intLst = twoDLst[row]
        if(len(intLst) == 1): # start of path
            minLst.append(intLst[0])
        else: # this will look at each list after starting row
            if(intLst[c] < intLst[c + 1]): 
                minLst.append(intLst[c]) # c index remains the same
            else:
                minLst.append(intLst[c + 1])
                c += 1 # c index goes up one

    return(minLst)

def main():
    fileName = 'small_triangle.txt' #'large_triagle.txt'
    infile = open(fileName, 'r')
    lst = infile.readlines() 
    intLst = []
    twoDLst = []

    for line in range(0, len(lst)): # Nested for loop that creates a 2d list from .txt file
        for num in lst[line].split(): # Reads each integer from specific line
            intLst.append(int(num))# This places each integer to an empty list
        twoDLst.append(intLst) 
        intLst = [] # Clears list for next line
    
    for i in minPath(twoDLst, intLst): # Output
        print(i)

# File name can be editted within main function
if __name__ == '__main__':
    main()
