# -*- coding: cp1252 -*-
####Question 1
####Level 1
####
####Question: Write a program which will find all such numbers which are
####divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both
####included). The numbers obtained should be printed in a comma-separated
####sequence on a single line.

##i = []
##
##for l in range (2000,3201):
##    if l%7 == 0 and l%5 != 0:
##        i.append(l)
##
##print i
##print len(i)
##
####Official Answer
##
##l=[]
##for i in range(2000, 3201):
##    if (i%7==0) and (i%5!=0):
##        l.append(str(i))
##
##print ','.join(l)

#########################

####Question 2
####Level 1
####
####Question:
####Write a program which can compute the factorial of a given numbers.
####The results should be printed in a comma-separated sequence on a single line.
####Suppose the following input is supplied to the program:
####8
####Then, the output should be:
####40320  (>) or less than (<

##i = raw_input("Give me an integer: ")
##l = 1
##
##while True:
##    try:
##        i = int(i)
##        break
##    except:
##        print "That's not an integer"
##        break
##
##while i >= 1:
##    l = l*i
##    i-= 1
##
##print l
##
####Official Answer
##
##def fact(x):
##    if x == 0:
##        return 1
##    return x * fact(x - 1)
##
##x=int(raw_input())
##print fact(x)

#########################

####Question 3 Level 1
####
####Question:
####With a given integral number n, write a program to generate a dictionary
####that contains (i, i*i) such that is an integral number between 1 and n
####(both included). and then the program should print the dictionary.
####Suppose the following input is supplied to the program:
####8
####Then, the output should be:
####{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

##d = {}
##i = int(raw_input("Give me an integer: "))
##for n in range (1,i+1):
##    d[n] = n*n
##
##print d
##    
####Official Answer
##
##n=int(raw_input())
##d=dict()
##for i in range(1,n+1):
##    d[i]=i*i
##
##print d

#########################

####Question 4 Level 1
####
####Question:
####Write a program which accepts a sequence of comma-separated numbers from
####console and generate a list and a tuple which contains every number.
####Suppose the following input is supplied to the program:
####34,67,55,33,12,98
####Then, the output should be:
####['34', '67', '55', '33', '12', '98']
####('34', '67', '55', '33', '12', '98')

##data = raw_input("Give me a list separated by commas: ")
##
##pre = map(int, data.split(","))
##lst = list(pre)
##print lst
##
##tup = tuple(pre)
##print tup
##
####Official Answer
##
##values=raw_input()
##l=values.split(",")
##t=tuple(l)
##print l
##print t

#########################

####Question 5
####Level 1
####
####Question:
####Define a class which has at least two methods:
####getString: to get a string from console input
####printString: to print the string in upper case.
####Also please include simple test function to test the class methods.

##class methods(object):
##    def __init__(self):
##        self.s = ""
##        
##    def getString(self):
##        self.s = raw_input("Input: ")
##
##    def printString(self):
##        print self.s.upper() 
##
##x = methods()
##
##x.getString()
##x.printString()
##
####Official Answer
##
##class InputOutString(object):
##    def __init__(self):
##        self.s = ""
##
##    def getString(self):
##        self.s = raw_input()
##
##    def printString(self):
##        print self.s.upper()
##
##strObj = InputOutString()
##strObj.getString()
##strObj.printString()

#########################

####Question 6
####Level 2
####
####Question: Write a program that calculates and prints the value
####according to the given formula: Q = Square root of [(2 * C * D)/H]
####Following are the fixed values of C and H: C is 50. H is 30. D is the
####variable whose values should be input to your program in a
####comma-separated sequence. Example Let us assume the following comma
####separated input sequence is given to the program: 100,150,180 The
####output of the program should be: 18,22,24

##import math
##
##class operations(object):
##    def __init__(self):
##        self.n = ""
##        self.r = ""
##
##    def getstring(self):
##        self.n = raw_input("Comma-separated numbers: ")
##        x = self.n
##        y = list(map(int, x.split(",")))
##        self.n = y
##
##    def maths(self):
##        c = 50
##        h = 30
##        d = self.n
##        i = 0
##        op = []
##        while i < len(self.n):
##            x = int(math.sqrt((2*c*d[i])/h))
##            op.append(x)
##            i+=1
##        self.r = op
##
##    def printout(self):
##        print self.r
##
##r = operations()
##r.getstring()
##r.maths()
##r.printout()

####Official Answer

##!/usr/bin/env python
##import math
##c=50
##h=30
##value = []
##items=[x for x in raw_input().split(',')]
##for d in items:
##    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
##
##print ','.join(value)

#########################

####Question 7 Level 2
####
####Question:
####Write a program which takes 2 digits, X,Y as input and generates a
####2-dimensional array. The element value in the i-th row and j-th column
####of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.
####Example
####Suppose the following inputs are given to the program:
####3,5
####Then, the output of the program should be:
####[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

##data = raw_input("Give me two digits separated by a comma: ")
##
##lst = map(int, data.split(","))
##
##x = [i for i in range(0,lst[0])]
##y = [i for i in range(0,lst[1])]
##
##Z = [[x[i]*y[j] for j in range(0,lst[1])] for i in range(0,lst[0])]
##
####R = []
####for i in range(0,lst[0]):
####    R.append([x[i]*y[j] for j in range(0,lst[1])]) - same loop but bigger
##    
##print Z
##
####Official Answer
##
##input_str = raw_input()
##dimensions=[int(x) for x in input_str.split(',')]
##rowNum=dimensions[0]
##colNum=dimensions[1]
##multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
##
##for row in range(rowNum):
##    for col in range(colNum):
##        multilist[row][col]= row*col
##
##print multilist

#########################

####Question 8
####Level 2
####
####Question: Write a program that accepts a comma separated sequence of
####words as input and prints the words in a comma-separated sequence after
####sorting them alphabetically. Suppose the following input is supplied to
####the program: without,hello,bag,world
####Then, the output should be:
####bag,hello,without,world

##data = raw_input("Give me a list of words: ")
##lst = map(str,data.split(","))
##R = ""
##lst = sorted(lst)
##for i in range(0,len(lst)):
##    R += (lst[i])
##    R += (",") if i+1<len(lst) else ""
##
##print R
##
####Official Answer
##
##items=[x for x in raw_input().split(',')]
##items.sort()
##print ','.join(items)

#########################

####Question 9
####Level 2
####
####Question£º Write a program that accepts sequence of lines as input and
####prints the lines after making all characters in the sentence
####capitalized. Suppose the following input is supplied to the program:
####Hello world Practice makes perfect Then, the output should be: HELLO
####WORLD PRACTICE MAKES PERFECT

##data = []
##i = 0
##print "Give me data, type BYE to stop"
##while True:
##    s = raw_input()
##    if s == "BYE":
##        break
##    data.append(s.upper())
##    i+=1
##    
##for i in range(0,len(data)):
##    print data[i]
##
####Official Answer
##
##lines = []
##while True:
##    s = raw_input()
##    if s:
##        lines.append(s.upper())
##    else:
##        break;
##
##for sentence in lines:
##    print sentence

#########################

##Question 10 Level 2
##
##Question:
##Write a program that accepts a sequence of whitespace separated words as
##input and prints the words after removing all duplicate words and
##sorting them alphanumerically. Suppose the following input is supplied
##to the program:
##hello world and practice makes perfect and hello world again
##Then, the output should be:
##again and hello makes perfect practice world

data = raw_input("Give me a sequence of words: ")
lst = map(str, data.split())

lst.sort()

for i in range(0,len(lst)):
    if lst[i] == lst[i-1]:
        lst[i] = ""

lst = filter(None,lst)

print " ".join(lst)

##Official Answer

s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
