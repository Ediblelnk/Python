#create new class Pet
class Pet:

	classVariable = "this is from the Pet Class"

	#init method
	def __init__(self, name, age):
		self._name = name
		self._age = int(age)

	#show method
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	#speak method
	def speak(self):
		print("I don't know what to say")

#create child class Cat
class Cat(Pet):

	classVariable = "this is from the Cat Class"

	#init class method because Cat requires different initialization variables
	def __init__(self, name, age, color):
		super().__init__(name, age) #calls pet __init__ method, do not include 'self'
		self._color = color.lower() #lower case

	#speak method different than parent/super class, need to redefine the method
	def speak(self):
		print("Meow")

	#show method different because of the new instance variable requirement, need to redefine the method
	def toString(self):
		print(f"I am {self._name} and I am {self._age} years old and I am {self._color}.")

	#get method for a variable that is local to cat class
	def getColor(self):
		return self._color

	#get method for a variable that is from pet class inherited to cat class
	def getAge(self):
		return self._age

	@classmethod
	def fromString(cls, catString): #a class method does not take an instance of a class as a variable, it takes the class itself
		name, age, color = catString.split('-')
		return cls(name, age, color)

	@staticmethod
	def isOverage(age): #a static method is a method that is essentially just a function for a class
		if int(age) > 15:
			return True
		return False

	def evaluate(self):
		return Cat.isOverage(self._age)

class Dog(Pet):

	#no init method because there is nothing new that need to be passed to create object Dog
	#speak method different than parent/super Class, need to redefine the method
	def speak(self):
		print("Bark")

#test the creation and use of class/methods

def main():
	#create pet class object instance
	p = Pet("Tim", 19)
	p.speak()

	#create child class 'cat' object instance
	c = Cat("Gerald", 19, "brown")
	c.speak()
	c.toString()

	#create another class, but via a class method
	c2 = Cat.fromString('Brush-14-blue')
	c2.toString()
	print(c2.evaluate())

	#create child class 'dog' object instance
	d = Dog("Doug", 6)
	d.speak()

	print(c.getAge())

	print(c.classVariable)

if __name__ == '__main__':
	main()