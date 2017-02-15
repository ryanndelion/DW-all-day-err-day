# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:27:00 2017

@author: admin
"""
#HW1
#from Week4Problem4 import transpose_matrix
#F = [0,10,20,30,40,50,60,70,80,90,100]
#C = []
#CApprox = []
#conversion = []
#def f_to_c(F):
#    for i in range (len(F)): 
#        C_i = round(((F[i]-32)*5/9.0),1)
#        C.append(C_i)
#    return C
#def f_to_c_approx(F):
#    for i in range (len(F)):
#        CApprox_i = round(((F[i]-30)/2), 1)
#        CApprox.append(CApprox_i)
#    return CApprox
#def get_conversion_table(F):
##    f_to_c(F)[i] = c
##    f_to_c_approx(F) = c_approx
#    for i in range (len(F)):
#        conversion_i = (F[i], f_to_c(F)[i], f_to_c_approx(F)[i])
#        conversion.append(conversion_i)
##    transpose_matrix(conversion)
#    return [[conversion[j][i] for j in range(len(conversion))] for i in range(len(conversion[0]))]
#    
#print get_conversion_table(F)


#HW2
#def max_list(inp):
#    max_list = []
#    for i in range (len(inp)):
#        max_i = max(inp[i])
#        max_list.append(max_i)
#    return max_list
#    
#def max_list(inp):
#    outp=[]
#    i = 0
#    while (i < len(inp)):
#           maxNum = -sys.maxint-1
#           j = 0
#           while(j < len(inp[i])):
#               if (inp[i][j]>maxNum):
#                   maxNum = inp[i][j]
#               j=j+1
#           outp.append(maxNum)
#           i=i+1
#    return outp
#print max_list( [[100] ,[1 ,7] ,[ -8 , -2 , -1] ,[2]]) 


#HW3
#def multiplication_table(N):  
#
##    for i in range (1,N+1):
##        for j in range (1, N+1):
##            a = i*j
##            list1.append(a)
#    if N <= 0:
#        return 'None'
#    else:
#        m = list(list(range(1*i,(N+1)*i, i)) for i in range(1,N+1))
#    return m
#        
#print multiplication_table(7)
#
#def multiplication_table(N):
#    if (N < 1):
#        return None
#
#    table = []
#    i = 1
#    i_pos = i-1
#    while i < N+1:
#        n = 1
#        n_pos=n-1
#        table.append([])
#        while n <= N:
#            num = i*n
#            table[i_pos].append(num)
#            n += 1
#            n_pos += 1
#        i += 1
#        i_pos += 1
#
#    return table
#    
#def multiplication_table(N):
#    if (N < 1):
#        return None
#    table = []
#    for i in range(1,N+1):
#        # This can actually be table.append(range(i,i*N+1,i))
#        row = []
#        for j in range(i,i*N+1,i):
#            row.append(j)
#        table.append(row)
#    return table


#HW4
#def most_frequent(numList):
#    d = dict()
#    new_list = []
#    frequency = 0
#    for c in numList:
#        if type(c)!= int:
#            return "One of the elements in the list is not an integer."
#        elif c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#
#    for k,v in d.items():
#        if v > frequency:
#            frequency = v 
#            new_list = []
#        else: 
#            pass
#        if v == frequency:
#            new_list.append(k)
#    return new_list
#    
#print most_frequent([1,2,1,2,1,2,1,0])
#
#def most_frequent(numList):
#    d={}
#    for i in numList:
#        if i not in d:
#            d[i]=1
#        else:
#            d[i]+=1
#    
#    maxNumList=[]
#    maxFreqList=[]
#    
#    finished=False
#    while not finished:
#        maxFreq=0
#        maxNum=0
#
#        for k,v in d.items():
#            if v>maxFreq:
#                maxNum=k
#                maxFreq=v
#        if d!={}:
#            del d[maxNum]
#        if maxNumList==[] or maxFreq in maxFreqList:
#            maxNumList.append(maxNum)
#            maxFreqList.append(maxFreq)
#        elif maxNumList!=[]:
#            finished=True
#    return maxNumList


#HW5
#def diff(p):
#    dp = {}
#    for k,v in p.items():
#        if k == 0:
#            pass
#        else:
#            v = k*v
#            k = k-1
#            dp[k] = v
#    return dp
#    
#print diff({0:-3, 1:12, 2:-2, 3:2, 10:2})






    