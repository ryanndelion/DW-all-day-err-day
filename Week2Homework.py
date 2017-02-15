# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:19:00 2017

@author: admin
"""
#Problem1
#def celcius_to_farenheit (C):
#    return (C*9.0/5)+32
#    
#C = int(raw_input ("What is the temperature in Celcius?"))
#print celcius_to_farenheit (C)


#Problem2
#from math import pi
#def area_vol_cylinder(radius,length):
#    area = (radius**2)*pi
#    volume = area*length
#    return (area, volume)
#    
#print area_vol_cylinder(1.0,2.0)


#Problem3
#def wind_chill_temp(ta, v):
#    twc=35.74+0.6215*ta-35.75*v**0.16+0.4275*ta*v**0.16
#    if v < 2:
#        return "Invalid wind speed"
#    if ta > 41:
#        return "Invalid temperature"
#    elif ta < -58:
#        return "Invalid temperature"
#    else:
#        return twc
#        
#print wind_chill_temp(5.3, 6)
    

#Problem4
#def bmi(weight,height):
#    kg=weight*0.45359237
#    metre=height*0.0254
#    BMI=kg/(metre**2)
#    return BMI
#
#print bmi(95.5, 50)


#Problem5
def investment_val(amount, annualRate, years):    
    futureInvestmentValue=amount*(1+annualRate/1200)**(years*12)
    return round(futureInvestmentValue, 2)
    
print investment_val(1000, 4.25, 1)
