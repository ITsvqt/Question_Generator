
#TODO: adding different lists requires renaming them
### Using list of dictionaries for each q&a pack
# every dictionary has 2 items
# 1st key - question, 1st value - question text
# 2nd key - answer  , 2nd value - the qeustion answer

#Core module
questions_and_answers = [
    {'question': 'What is programming ?', 
     'answer' : '-Creating sequence of instructions to enable the computer to do something. '}, # 0
    
    {'question': 'Why do we write programs ?',
     'answer' : '- We write programs to automate tasks and solve problems with a computer. '}, # 1
    
    {'question': 'What are the main two components of a program ?',
     'answer' : '- Data - the information the program processes\n\n\
- Algorithm - the instructions that process the Data'}, # 2
    
    {'question': 'How does Computing Works ?',
     'answer' : '-At its core, a computer is a machine that receives input, processes it, stores it, and produces output.'}, # 3
    
    {'question': 'How are Python programs processed ?', 
     'answer' : '-An interpreter reads and runs the code line by line at runtime.'}, # 4
    
    {'question': 'Explain what conditional statements are and their usage.',
     'answer' : '-Conditional statements are what allow programs to react to different situations.'}, # 5
    
    {'question': 'Explain what loops are and how they work.', 
     'answer' : '-A loop is a programming construct that repeats a block of code multiple times.'}, # 6
    
    {'question': 'What is a list in Python? How is it different from a string ?',
     'answer' : '-A list is a flexible, mutable container that can hold any mix of items.\n\
- A string is text — a fixed, immutable sequence of characters.'}, # 7
    
    {'question': 'Can you use a list comprehension to transform or filter a string ?', 
     'answer' : '-Since strings are iterable, list comprehensions treat them like a list of characters.'}, # 8
    
    {'question': 'What is Syntactic Sugar ? ',
     'answer' : '-It\'s a shortcut - under the hood, the language translates it into something more verbose that it could already do.'}, # 9
    
    #todo remove this question
    {'question': 'Can you use a list comprehension to transform or filter a string ?', 
     'answer' : '-Since strings are iterable, list comprehensions treat them like a list of characters.'}, # 10
    
    {'question': 'What\'s the difference between function and method ?',
     'answer' : '-Standalone block of code that can be called independently.\n\
-Method is function that belongs to an object or class. It\'s called on an instance (or the class itself) and typically operates on that object\'s data.'}, # 11
    
    {'question': 'What are the four corners of a matrix ?',
     'answer': '[0][0]\n\
                [0][len-1]\n\
                [len-1][0]\n\
                [len-1][len-1]'}, # 12

    {'question': 'What\'s the difference between parameter and argument ?',
     'answer': '-Parameters are variables defined in the method signature.\n\
-Arguments are the actual values passed to the method when it is called.'}, #13
    
    {'question': 'What is a method in programming ?',
     'answer': '-A method is a defined block of code that encapsulates reusable logic.\n\
-It has a name, may return a value (or be void), and can accept arguments to perform a specific task.'}, #14
    
    {'question': 'What are the key reasons for using methods  ?',
     'answer': '-Methods are used for code reusability, easier debugging, simpler maintenance, and to create more organized and understandable programs.'}, #15
    
    {'question': 'Explain the concept of method overloading. ',
     'answer': '-Method overloading is defining multiple methods with the same name but different parameter lists—either in number, type, or both.\n\
-This allows a single method name to support related behaviors.'}, #16
    
    {'question': 'Why is debugging important, and when does it primarily occur (compile-time vs. run-time) ?',
     'answer': '-Debugging is the process of identifying and fixing errors in code.\n\
-It primarily takes place at run-time, unlike compile-time errors that are caught before execution.'}, #17
    
    {'question': 'What is a breakpoint, and how is it used in debugging ?',
     'answer': '-A breakpoint is a marker that pauses program execution at a specific line.\n\
-It allows developers to inspect variables and trace how the program is behaving step by step.'}, #18
    
    {'question': 'Why is it generally good practice for a method to perform only one specific task ?',
     'answer': '-Keeping methods focused on one specific task improves readability, makes testing easier, and simplifies future changes or extensions.\n\
-This approach supports clean and modular code.'}, #19
    
    {'question': 'Explain the difference in how primitive and reference types are passed to methods in Python.',
     'answer': '-Yes, but Python doesn\'t use that terminology. The concept maps to how Python treats every object.\n\
-The distinction isn\'t in the type system — it\'s in whether the object allows mutation.'}, #20
    
    {'question': 'What is the "single responsibility principle" as it applies to methods ?',
     'answer': '-The single responsibility principle means a method should have only one reason to change.\n\
-It should focus on a single task or functionality to promote clean, maintainable code.'}, #21
    
    {'question': 'Why is the order of method definitions in a Java program not technically significant during execution ?',
     'answer': '-Method definition order does not affect execution because the compiler scans and processes all method declarations before runtime.\n\
-Methods can be defined in any order and still be called correctly.'}, #22
    
    {'question': 'What\'s a scope ?',
     'answer': '-Determines the visibility and lifetime of names.\n\
-Concept to avoid name collisions.\n\
-Following the local,enclosing,global,built in rule (LEGB).'}, #23
    
    {'question': 'What\'s a module ?',
     'answer': '-A python file that can be imported into another file. Used to organize complex code.\n\
-It contains constants, classes, functions,guards.'}, #24
   
    {'question': 'What is a multidimensional list ?',
     'answer': 'Lists that have nested lists for values.'}, #25
    
    {'question': 'How can we iterate through a multidimensional list ?',
     'answer': '-Nested loop.'}, #26
    
    {'question': 'How many \'dimensions\' can we have ?',
     'answer': '-As many as i want. 3 is the reasonable limit.'}, #27
    
    {'question': 'What is a namespace in python ?',
     'answer': 'A python namespace is represented by a dictionary that maps names to objects,\n\
organize variables, and determine their scope.'}, #28    
    
    # {'question': '',
    #  'answer': ''}, #29
    
    # {'question': '',
    #  'answer': ''}, #30    
]

