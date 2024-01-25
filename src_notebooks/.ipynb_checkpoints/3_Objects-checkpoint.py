# # Objects
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * define objects
# * use subclasses and superclasses
# :::
#
# ## Object-oriented programming
# Python is an example of an *object-oriented* programming language. That means that we primarily (and actually, *only*) work with objects. Everything in Python is an object. An object is an entity that contains data along with associated metadata and/or functionality. We can define objects for anything. 
#
# Without knowing it, you have been using objects for the past few weeks. For example, a `list` is an object in Python, and 
#
# A minimal version of an object contains
#
#
# ```python
#
# ```
#
#
#
#
# Everything in Python is an object
#
# :::{admonition} Objects in Python
# :class: note
# Everything in Python is an object.
# :::
#
#

# ## What is object-oriented programming?
# An object in object-oriented programming has two things:
# 1. *attributes*
# 2. *methods*
#

# ## Methods and functions
# You can think of the *methods* of a class as the functions that operate on that class.

# ## The `__init__` function
# Every class in Python has a fixed number of functions

# ## A simple class
# Let's start with a basic example. We can define a class for a circle that is centered at the origin. A circle is defined by it's radius. In the `__init__` method

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)


# ## Scope
#

# ## Class inheritance
# Using inheritance, we can define a class that *inherits* all properties and methods from another class. This is convenient if there is some hierarchy of classes. We call the class that inherits the *child class* or the *derived class* and the class from which we inherit the *parent class* or *base class*. You can think of a derived class as a specialized version of the base class. 
#
# ![inheritance](https://files.realpython.com/media/ic-basic-inheritance.f8dc9ffee4d7.jpg)
#
# For example, we could have a parent class that defines a person, and a child class that defines a student. This works because a student is always a person, but the reverse does not necessarily hold (a person is not always a student). We can first define - in the same was as before - our `Person` class. You have already learned that you can create an object of this class by invoking the `__init__` function, i.e., `x = Person("John", "Doe")`. Now, we have created an object that corresponds to a person, but not yet to a student.

# +
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


# -

# The derived class of this would have a first name and last name as well. In the simplest case, we can make a derived class as follows. The parentheses after `Student` indicate that this class inherits from `Person`.

class Student(Person):
    pass


# We can create a new student now, just like we created a person before.

x = Student("Harry", "Potter")
x.printname()


# The child class has inherited the properties of the parent class, including it's `__init__` and `printname` methods. We can **override** the `__init__` method of the parent class by defining a new `__init__` method in the derived class. Within that method, you can first call the `__init__` method of the parent class, in this case to set the first name and last name of the student.

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)   # You could here also use super() instead of Person


# Moreover, you can extend the `__init__` method, and add additional attributes. For example, to add a study program to the student, we just adapt the `__init__` method of the `Student` class (but not the `Person` class) and set an attribute. 

# +
class Student(Person):
    def __init__(self, fname, lname, program):
        Person.__init__(self, fname, lname)   
        self.program = program
        
x = Student("Harry", "Potter", "sorcery")


# -

# We can again **override** the original `printname` method, or define completely new methods.

# +
class Student(Person):
    def __init__(self, fname, lname, program):
        Person.__init__(self, fname, lname)   
        self.program = program
    
    def printname(self):         # Overrides method of Person
        print(self.firstname, self.lastname, self.program)
    
    def printprogram(self):      # New method specific to Student
        print(self.program)
        
x = Student("Harry", "Potter", "sorcery")
x.printname()
x.printprogram()
# -

# If you think about it, every class - including the `Person` class that we defined - inherits from other classes. In essence, everything in Python is an object, and any new class that you define inherits from Python's `object` class. Even though we never explicitly define them, the `Person` class has a number of methods that we can override. These can be listed using the built-in `dir` function. 

dir(Person)


# Python puts no restrictions on the level of inheritance that you use, and we can in fact use *nested inheritance* where a new derived class inherits from a class that is itself derived from a base class. In our example, we could define a derived class for bachelor students, i.e.

# +
class BachelorStudent(Student):
    def __init__(self, fname, lname, program, year):
        Student.__init__(self, fname, lname, program)
        self.year = year
        
    def printname(self):
        print(self.firstname, self.lastname, self.program, self.year)

x = BachelorStudent("Frenk", "Saminis", "TM", 1)
x.printname()
# -

# :::{admonition} Exercise
# :class: tip
# In this exercise you're going to define a (small) zoo of animals. Your task is to design a base class `Animal` and at least five different species of animals that inherit from this base class. Think carefully about the following
# * What is the common denominator between animals? 
#
# Animals should be able to do at least the following
# * make sounds
# * have a speed
# * provide geographic origin
#
# In addition, we want you to write a function that determines who will win a race, given two input animals.
# :::




