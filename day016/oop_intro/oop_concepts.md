# [Object-Oriented Programming in Python](https://www.freecodecamp.org/news/object-oriented-programming-in-python/)

Four core aspects of a generic OOP framework:
    - Encapsulation, 
    - Abstraction, 
    - Inheritance, 
    - Pymorphism.

## Classes and objects

A **class** is a collection of instance variables and methods that define a particular object type.
Attributes are the names given to the variables that make up a class.

A class instance with a defined set of properties is called an  **object**.

Note that one class can be used to construct as many objects as needed.

## Encapsulation

Encapsulation is the process of preventing clients from accessing certain properties by setting as private. 

Private attributes are inaccessible attributes. We use two undescores to declare private characteristics.

To access private attributes we need to define the **set** and **get** methods.

## Inheritance

A class's ability to inherit methods/or characteristics from another class is known as **inheritance**.

The subclass or child class is the class that inherits. The superclass or parent class is the class from which methods and/or attributes are inherited.

## Polymorphism

Polymorphism means "something that takes on multiple forms".

In our context, **polymorphism** refers to a subsclass's ability to adapt a method that already exist is its superclass to meet its needs.

A subclass can use a method from its superclass as is or modify it as needed.

## Abstraction

Abstraction is a method (not supported directly in Python) that allows for abstraction.

If an abstract method is declared in a superclass, subclasses that inherit from the superclass must have their own implementation of the method.

## Method Overloading

Overloading it simply refers to the use of many methods with the same name that take various numbers of arguments within a single class.

## Method Overriding

When a method with the same name and arguments is used in both a derived class and a base or super class, we say that the derived class method "overrides" the method provided in the base class.

## Reference

All the concepts above can be found here ==> https://www.freecodecamp.org/news/object-oriented-programming-in-python/

(All concepts described here are only summaries of the content in question.)