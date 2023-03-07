'''def func(*args,**kwargs):
    print("servus",args,kwargs)

def fuc(a):
    print("servus")

def fug(b):
    print(b)

def ful(c):
    print("servus",c)

func("hey")
func("neg",25,"creamnog",sieben=8)
fuc("hi")
fug("jo")
ful("tek")


def myrand(request,*args,**kwargs,):
    print(kwargs,request,*args)

#path("samam/:dda")
myrand("request" ,id='iwas',(349))'''
def myFunction(a,b,c,*args,**kwargs):
    return print(a,b,c,args,kwargs)

myFunction(*(1,2,3,4,5,6,7),k=3)
'''
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("jeff",2)
print(miles.speak("figgernudl"))



class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width
# Here we declare that the Square class inherits from 
# the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

def sum(*args,**kwargs):
    sus=0
    args = list(args)
    args[0]=100
    for zahl in args:
        sus = sus+zahl
    print(sus)
sum(*[4,2,3,5])


def zeas(**kwargs):
    print("Hi",end=" ")
    for key,zuk in kwargs.items():
        print(zuk,end=" ")

zeas(Hi="Moin",Figg="fliege", aua="arschdehner")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()



#---------------------------------
import random

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
                numbers[i],numbers[j] = numbers[j],numbers[i]
    return numbers

def find_median(numbers):
    sorted_numbers = bubble_sort(numbers)
    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
    else:
        median = sorted_numbers[len(sorted_numbers) // 2]
    return median

def find_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    median = find_median(random_numbers)
    average = find_average(random_numbers)
    print("Die zufälligen Zahlen sind:", random_numbers)
    print("Der Median ist:", median)
    print("Der Durchschnitt ist:", average)
    
#---------------------------------
import functools

def muc(f):
    @functools.wraps(f)
    def wrapper(*args,**kwargs):
        print("luggugugug")
        f(*args,**kwargs)
    return wrapper

@muc
def add(a,b):
    return print(a + b)

add(3,8)

#-----------------------------------


class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.length*self.length}"
        
    
r = Rectangle(3,4,k=3)
print(r)
def bubble(**loc):
    print("Servus",end=" ")
    for key, z in loc.items():
        print(z,end=" ")

bubble(serwws="hello")'''