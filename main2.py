 # Section 1: The Way of the Program
    #  1. What is a computer program?
        #A computer program is a set of instructions written in a programming language that tells a computer how to perform a specific task.

    #   2. Explain the difference between source code and output.
        #Source code: The instructions written by a programmer in a programming language.
        # Output: The result produced when the program is executed.

    #   3. Name two types of errors that can occur in a Python program.
        #1. Syntax errors – mistakes in the structure or rules of Python.
        #2. Runtime errors – errors that occur while the program is running.
    
    #   4. What is the role of the Python interpreter?
        #The Python interpreter reads and executes Python code, translating instructions into actions the computer can perform.

    #   5. Write a Python statement that displays Welcome to Python.
        # print("Welcome to Python")

# Section 2: Variables, Expressions and Statements
    # 1. What is a variable? Give one valid Python variable name.
        # A variable is a named location used to store data in a program.
        # student_name = "John"

    # 2. Output of x = 4; x = x + 3; print(x)
        # Output: 7. We added 3 to the initial value of x (4), resulting in 7.
        # x = 4
        # x = x + 3
        # print(x) # 7
    
    # 3. Explain the difference between an expression and a statement.
        # - Expression: A combination of values, variables and operators that produces a value.
        # - Statement: An instruction that performs an action in a program.
        # 5 + 3 is an expression, 
        # while print(5 + 3) is a statement.

    # 4. Write an expression to calculate the area of a rectangle using length and width.
        # lenght * width
        
    # 5. What is wrong with the variable name 2score?
        # A Python variable name cannot begin with a number. It should begin with a letter or underscore.
        
# Section 3: Functions
    # 1. What is a function in Python?    
        # A function is a reusable block of code designed to perform a specific task. It runs when it is called.
    
    # 2. Write a function named greet that prints Hello.
        # def greet():
        #     print("Hello")
    
    # 3. Explain the purpose of parameters in a function.
        # Parameters allow a function to receive data or values when it is called, making the function more flexible and reusable.

    # 4. What is the difference between defining and calling a function?
        # - Defining: Creating a function using the def keyword.
        # - Calling: Executing the function by writing its name followed by parentheses.
        
    # 5. Write a function call that passes 5 to a function named double.
        # double(5)
    
# Section 4: Conditionals
    # 1. What is the purpose of an if statement?
        # An if statement is used to make decisions in a program by executing a block of code only when a specified condition is true.

    # 2. Write an if statement that prints Adult when age is at least 18.
        # age = 20
        # if age >= 18:
        #     print("Adult")
    
    # 3. Explain the difference between elif and else.
        # - elif checks another condition when the previous if or elif condition is false.
        # - else executes when all previous conditions are false.

    # 4. What does the expression 7 > 3 and 2 > 5 evaluate to?
        # Answer: False

    # 5. Write a conditional that prints Even if a number is divisible by 2 and Odd otherwise.
        # number = 4
        # if number % 2 == 0:
        #     print("Even")
        # else:
        #     print("Odd")
        
#Section 5: Recursion
    # 1. What is recursion?
        # Recursion is a programming technique in which a function calls itself to solve a problem.

    # 2. What is a base case in a recursive function?
        # A base case is the condition that stops a recursive function from calling itself repeatedly.

    # 3. Explain what may happen if a recursive function has no reachable base case.
        # The function may continue calling itself indefinitely until Python raises a RecursionError because the maximum recursion depth has been exceeded.

    # 4. Write a recursive function that returns the factorial of a non-negative integer.
        # def factorial(n):
        # if n == 0:
        #     return 1
     # else:
     #     return n * factorial(n - 1)
     
    #  5. State one difference between recursion and iteration.
        # Recursion involves a function calling itself, while iteration involves repeating instructions using loops such as for and while.
        
# Section 6: Fruitful Functions
    # 1. What is a fruitful function?
        # A fruitful function is a function that performs a task and returns a value using the return statement.

    # 2. How does return differ from print inside a function?
        # - return sends a value back to the part of the program that called the function.
        # - print displays a value on the screen but does not send it back as a function result.

    # 3. Write a function square(n) that returns n multiplied by itself.
        #     def square(n):
            #     return n * n
            
    # 4. What value is assigned to result after result = max(3, 9)?
        # Answer: 9
     
    # 5. Write a function that accepts two numbers and returns their average.
        # def average(a, b):
        #     return (a + b) / 2
        
# Section 7: Iteration
    # 1. What is iteration in programming?
        # Iteration is the process of repeatedly executing a block of code until a specified condition is met or a sequence is completed.

    # 2. Write a for loop that prints numbers 1 through 5.
        # for i in range(1, 6):
            # print(i)
            
    # 3. Explain one difference between for and while loops.
        # - A for loop is commonly used when the number of repetitions or items in a sequence is known.
        # - A while loop repeats as long as a specified condition remains true.
        
    # 4. What is the purpose of break in a loop?
        # The break statement is used to immediately terminate a loop, even if the loop condition is still true.

    # 5. Write a while loop that counts down from 3 to 1.
        # count = 3
        # while count > 0:
        #     print(count)
        #     count -= 1
        
# Section 8: Strings
    # 1. A string is a sequence of characters enclosed in single or double quotation marks.

    # 2. p
    
    # 3. String slicing is the process of extracting a portion of a string using index positions.

    # 4. print("hello".upper())
    
    # 5. 6

# Section 9: Lists
    # 1. A list is an ordered and changeable collection of items written using square brackets [].

    # 2. languages = ["Python", "Java", "C++"]
    
    # 3. items[1]
    
    # 4. append() adds an item to the end of a list, while remove() deletes a specified item from a list.

    # 5. 30
    
# Section 10: Dictionaries
    # 1. A dictionary is a collection of key-value pairs used to store data.
    
    # 2. student = {"name": "John", "age": 20}
    
    # 3. student["name"]
    
    # 4. The old value is replaced with the new value.

    # 5. A list uses numerical indexes to access items, while a dictionary uses keys.

# Section 11: Tuples
    # 1. A tuple is an ordered collection of items that cannot be changed after creation.
    
    # 2. numbers = (2, 4, 6)
    
    # 3. Tuples are immutable, while lists are mutable.
    
    # 4. 8

    # 5. No. Tuples are immutable, so their elements cannot be directly changed.
    
# Section 12: Classes and Objects
    # 1. A class is a blueprint used to create objects.

    # 2. An object is an instance of a class.
    
    #  3. class Student:
                # pass
                
    # 4. A class is a blueprint, while an instance is an individual object created from that class.

    # 5. The __init__ method initializes an object's attributes when the object is created.
    
# Section 13: Classes and Functions
    # 1. A function can create an object by calling the class constructor and returning the object.

    # 2. class Student:
        #     pass   
     # def make_student():
        #     return Student()    
        
    # 3. A function outside a class is a regular function, while a function inside a class is called a method.

    # 4. A function accepts an object as an argument to access its attributes and methods.

    # 5. def display_name(obj):
        #     print(obj.name)   
        
# Section 14: Classes and Methods
    # 1. A method is a function defined inside a class.

    # 2. self refers to the current instance of a class.
    
    # 3. class Dog:
        # def bark(self):
            #print("Woof")
    
    # 4. pet.bark()
    
    # 5. An instance attribute stores data belonging to an object, while a method performs an action.
    
# Section 15: Inheritance
    # 1. Inheritance allows a child class to acquire the attributes and methods of a parent class.

    # 2. class Car(Vehicle):
    #     pass
            
    # 3. It promotes code reusability.

    # 4. Method overriding occurs when a child class provides its own implementation of a method already defined in its parent class.

    # 5. super() allows a subclass to access methods and the constructor of its parent class.        
    
# Section 16: Analysis of Algorithms
    # 1. Algorithm efficiency refers to how well an algorithm uses computer resources, especially time and memory.

    # 2. Time complexity measures how an algorithm's execution time changes as the input size increases.

    # 3. O(n) means the execution time increases proportionally to the size of the input.

    # 4. O(n) scales better because its growth rate is slower than O(n²) for large inputs.

    # 5. Space complexity matters because it measures the amount of memory an algorithm requires.