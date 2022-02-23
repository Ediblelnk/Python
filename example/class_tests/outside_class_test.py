#need to say what class to import, like so:
import class_tests 	#do NOT include .py at end
from class_tests import Cat #import specific classes of functions using from
from class_tests import * #import all classes and functions from a module
#generally good advice to not use from _ import *, could import functions or classes that conflict namewise with other classes

#test the creation and use of class/methods

#create pet class object instance
p = Pet("Tim", 19)
print(f"I am {p._name} and ", end='')
p.speak()

#create child class 'cat' object instance
c = Cat("Gerald", 19, "brown")
c.speak()

c1 = Cat.fromString("Gatsby-14-tan")
print(f"{c1._name} is {c1._color}")

#create child class 'dog' object instance
d = class_tests.Dog("Doug", 6) #can still use references with file name
d.speak()