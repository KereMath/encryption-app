#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n=len(s)
    s=list(s)
    start=0
    for i in range(n):
        if s[i]=="":
            s.pop(i)
    n=len(s)
    a=n**(1/2) 
    a=int(a)
    s1=""
    s2=[]
    mat=[]
    if a*a==n:
        for i in range(a):
            row=[]
            for j in range(a):
                if start<n:
                    row.append(s[start])
                    start+=1
                else:
                    row.append("")
            mat.append(row)    
        
        mat1=[]
        for i in range(a):
            row=[]
            for j in range(a):
                row.append(mat[j][i])
                
            
            mat1.append(row)    
            
        
        for i in range(a):
            for j in range(a):
                s2.append(mat1[i][j])
                if j==a-1:
                    s2.append(" ")
            
        for i in range(len(s2)):
            if s2[i]!="":
                s1+=s2[i]
                
                
                    
                
            else:
                s1+=" "
            
    elif a*(a+1)>=n:
        for i in range(a):
            row=[]
            for j in range(a+1):
                if start<n:
                    row.append(s[start])
                    start+=1
                else:
                    row.append("")
            mat.append(row)    
        
        mat1=[]
        for i in range(a+1):
            row=[]
            for j in range(a):
                row.append(mat[j][i])
                
            
            mat1.append(row)    
            
        
        for i in range(a+1):
            for j in range(a):
                s2.append(mat1[i][j])
                if j==a-1:
                    s2.append(" ")
            
        for i in range(len(s2)):
            if s2[i]!="":
                s1+=s2[i]
                
                
                    
                
            else:
                s1+=" "
            
    else:     
        
        for i in range(a+1):
            row=[]
            for j in range(a+1):
                if start<n:
                    row.append(s[start])
                    start+=1
                else:
                    row.append("")
            mat.append(row)    
        
        mat1=[]
        for i in range(a+1):
            row=[]
            for j in range(a+1):
                row.append(mat[j][i])
                
            
            mat1.append(row)    
            
        
        for i in range(a+1):
            for j in range(a+1):
                s2.append(mat1[i][j])
                if j==a:
                    s2.append(" ")
            
        for i in range(len(s2)):
            if s2[i]!="":
                s1+=s2[i]
                
                
                    
                
            else:
                s1+=" "
        
        
        
        
        
    s3=[]
    for i in range(len(s1)):
        s3.append(s2[i])
    for i in range(len(s3)):
        if i<len(s3)-1:
            if s3[i]==" ":
                if s3[i+1]==" ":
                    s3[i+1]==""
    s4=""                
        
    s4="".join(s3)        
    return s4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
