#import feature.copyright

#print(feature.copyright.date_of_copyright)

#import feature.subfeature.calculator
#import feature.copyright


#print(feature.subfeature.calculator.subtract(10,5))
#print(feature.copyright.date_of_copyright)

#from feature.subfeature import calculator
#print(calculator.subtract(2,1))

from feature.subfeature.calculator import subtract
print(subtract(1,2))