# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 12:24:25 2017

@author: admin
"""
#HOMEWORK1
#def check_value(n1,n2,n3,x):
#    if x>n1 and x>n2 and x<n3:
#        return True
#    else:
#        return False
#    
#print check_value(10,4,8,7)

#HOMEWORK2
#def farenheit_to_celsius(F):
#    C = (F-32)*float(5)/9
#    return C
#
#def celsius_to_farenheit(C):
#    F = C*float(9)/5 + 32
#    return F
#
#def temp_convert(type, temp):
#    if type == "F":
#        return celsius_to_farenheit(temp)
#    elif type == "C":
#        return farenheit_to_celsius(temp)
#    else: return None
#
#print temp_convert("F", 0)

#HOMEWORK3
#def get_even_list(ls):
#    evenlist = []
#    for i in range(len(ls)):
#        if ls[i]%2 == 0:
#            evenlist.append(ls[i])
#        else:
#            pass
#    return evenlist
#
#print get_even_list([1,2,3,4,5,6,7,8])

#HOMEWORK4
#def is_prime(n):
#    x = True 
#    import math as m 
#    if n<2:
#        return False
#    if n == 2:
#        return True
#    
#    for i in range (2, int(m.sqrt(n))+1, 2):
#        if n%i == 0:           
#             return False
#    return True
#    if x:
#        return True
#    else:
#        return False
#
#print is_prime(9) 
    
#HOMEWORK5
#import math
#def f(t, y):
#    return 3.0+math.exp(-t)-0.5*y
#
#def approx_ode(h,t0,y0,tn):
########## h - step size
########## t0 - initial t value (at step 0)
########## y0 - initial y value (at step 0)
########## tn - t value at step n
#
########## Add you code below this line
########## Return your answer correct to 3 decimal places
#    y = y0 
#    t = t0
#    for i in range (int(tn*10)):
#        y = y + h*(f(t, y))
#        t =t + h
#    return round(y, 3)
#
#print approx_ode(0.1,0,1,2.5)

######### Ignore code below this line ######################################



