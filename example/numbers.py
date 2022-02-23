ex_int = 3
print(type(ex_int), '=', ex_int)
ex_float = 3.0
print(type(ex_float), '=', ex_float)
ex_complex = 3.0j
print(type(ex_complex), '=', ex_complex)

'Common Operations'
#sum
8 + 3 #= 11

#difference
8 - 3 #= 5

#quotient
8/3 #= 2.66666666666

#floored quotient
8//3 #= 2

#remainder
8%3 #= 2

#negated
-3
#unchanged
+3

#absolute value
abs(-3) #= 3

#converted to int
int() #= 0
int(3.9) #= 3, truncates towards 0
int('10', 2) #= 2, first arg can be string of int value, second arg is base

#convert to float
float() #= 0.0
float('3e-4') #= 0.0003
float('3e4') #= 30000.0
float(3) #= 3.0
float('3') #= 3.0
float('-Infinity') #= -inf

#complex number
c = 3-3j
complex(1, 1) #= 1+j
complex(1) #= 1+j
complex('1-5j') #= 1-5j
complex('inf-j') #= inf-j
c.conjugate() #3+3j, conjugate of 3-3j

#divmod
divmod(8, 4) #= (2, 0), which is(8//4, 8%4)

#powers / exponents
pow(8, 3) #= 8^3 = 512
8**3 #= 8^3 = 512
pow(0, 0) #= 1, which is common for programming languages