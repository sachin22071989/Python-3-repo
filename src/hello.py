"""
Multiple
line
comments before
"""
name = """Sachin  Kumar"""
name1='''sachin kumar
'''
print("before if block")
if True:
				print(">>>>>IF<<<<<<<< ")
				print(">>>>>Block<<<<<")
print("After IF block and befor false block")
if False:
				print("False Block")
print("After false block")
print(name, name1)
"""
Multiple
line
comments
"""
msg = "welcome to python"; n = 23
print(msg, n)

import keyword
print('sachinkumar'.isidentifier())
n = None
print(n==None, '------>>>	None == null')
print(n is None)
x=9789
print(type(x))
print(isinstance(x,int))
print(x)

print('only int, float and complex class is available for number literals')

""" int is unlimited """
"""0b / 0B prefix Binary Number 0 and 1"""
y=0b110101010
print(y, '----->>>0 and 1 prefix 0B/0b for binary number')
del(y)

""" Decimal number 0 to 9 """
y=9876543210
print(y, '------->>>0 to 9 Decimal numbers')
""""del(y)"""

"""0c / 0C prefix Octal Number 0 and 7
y=0C10"""
print(y, '----->>>0 and 7 prefix 0C/0c for Octal number')
del(y)

""" 0x/ 0X prefix for HexaDecimal number 0 to 9 and A to F """
y=0x15487ABC
print(y, '------->>>0 to 9 and A to F for HexaDecimal numbers')
del(y)

""" Float 
after 15 decimal places number will be inaccurate """
y=2.1542689758412561234587888
print(y, '----->>>after decimal only 15 places number will be accurate')
del(y)
y=2.23456e2
print(y)
del(y)
y=2.23456e-2
print(y)
print(type(y))
print(isinstance(y,float))
del(y)
y=3+4j
print(y.real)
print(y.imag)
del(y)
y=3.4j
print(y.real)
print(y.imag)
print(type(y))
print(isinstance(y, complex))
del(y)

veriable1 = veriable2 = veriable3 = "Hello"
print(veriable1+" "+veriable2+veriable3)
veriable5 = "SachinKumar"
print("sub string : "+veriable5[0:6])
print("Sub string : "+veriable5[6:])

nameList = ["sachin","kumar","Rohit"]
print(nameList)
print(nameList[2])
print(len(nameList))
nameList[1] = "Kashyap"
print(nameList)

del(nameList[2])
print(nameList, len(nameList))

ageList = ["12","20","30","40","50","40"]
minimum = min(ageList)
print(minimum)
print(max(ageList))
print(ageList.count("40"), "----->>> count the number of 40 in the list")