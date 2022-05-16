import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
import math
import random
#Functions for the main program
def get_word_to_number(word):
    word = word.replace(" ","").lower() #remove spaces and make lowercase
    ns=""
    n = [ord(x) - 96 for x in word]  #gets a number for each letter
    for i in range(np.size(n)):
        ns+=str(n[i])
    #print(f"Word to number generates\n{ns}")
    return format(int(ns), 'b');
#expend the binary number to fit the half length of the matrix
def expend_binary(b):  #repeats adding the binary on itself until it reaches size 30x30
    min_size = 50
    ns=""
    while len(ns)<((min_size**2))-1:
        for i in range(len(b)): 
            ns+=b[i]
    #print(f"expend_binary generates\n{ns}\n size:",len(ns))
    return (ns)
#Random orientation dependent on the first 2 digit x=0, y=0, x=y or x=-y
def matrix_construct(a):
    min_size = 30
    if len(a)>=((min_size**2)/2):
        size=round(np.floor(np.sqrt(len(a))))
    else:
        size=min_size
    b=a[0]+a[1]
    size += np.mod(size,2)
    a=[int(x) for x in list(a)]
    m=np.zeros((size,size))
    count=0
    #print("\nSize {}\n".format(size))
    if b=="00" or b=="11":   #x==y=-y
        #x=y #creates a triangle matrix
        for i in range(size):
            for j in range(i):
                m[i][j]=a[count]
                m[j][i]=a[count]
                count+=1
        if b=="11": #mirror the matrix horizontally
            m=np.fliplr(m)
            
    elif b=="01" or b=="10": #y==x=0
        for i in range(size):
            for j in range(round(size/2)):
                m[i][j]=a[count]
                m[i][size-1-j]=a[count]
                count+=1
        if b=="10": #mirror the matrix diagonally
            m=np.transpose(m)
            print(" ")
    #print("Constructed matrix \n",m) 
    return m