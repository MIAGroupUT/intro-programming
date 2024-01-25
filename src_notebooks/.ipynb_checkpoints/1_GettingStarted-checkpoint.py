# # Getting started
# ####  Version Jan 23, 2024
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * be able to install and use Anaconda as your Python distribution 
# * understand the role of the Python interpreter in programming
# * find and use the command line interface on your computer
# * perform basic arithmetic operations using the Python interpreter
# * define variables in Python
# * work with floating point numbers, integers, and string variables
# * know the difference between tuples, lists, sets, and dictionaries
# * index and slice tuples and lists
# :::
#
# ## What is Python? 
# Python is a programming language that allows you to write software programs. By programming in Python you can tell the computer how to do things. Just like Python, there are many other programming languages out there. You might have heard about some of them, like `C`, `C++`, `Java`. Alternatively, it might be that you have heard of (or used) `Matlab`. In general, programming languages have a lot of similarities. They all allow you to work with data, and to change that data into something else. They (almost) all have ways to visualize your data. However, there are also some differences. 
#
# ```{note} Python
# Python is an interpreted, *object-oriented*, high-level programming language with dynamic semantics.
# ``` 
#
# It is important to realize that Python is *object-oriented* and that everything in Python is an object. We will explain later what this means.
#
# ## How do I start?
# Python is a programming language that doesn't natively come with a programming environment. There are many ways to install and use Python on your own computer, but in this course we will use three essential components to get you up and running with Python.
# * We will use **Anaconda** as the Python distribution and environment manager.
# * We will use **Visual Studio Code** as the integrated development environment (IDE).
# * We will use **Jupyter Notebooks** to develop interactive notebooks.
#
# Don't worry if these words don't mean a lot yet. We'll introduce all these tools step-by-step so that you get a good understanding what everything is and that you'll be comfortable using Python in your studies.
#
# ```{warning}
# Whenever we provide instructions on how to install software, please closely follow the order indicated.
# ```

# ## Installing Anaconda
# The first step is to download Anaconda, a widely used Python distribution. Anaconda contains a lot of very useful functionality:
# * The newest versions of Python
# * A powerful package manager
#
# Anaconda is free. To download it, go to [the Anaconda website](https://www.anaconda.com/download) and select `Download`. This will download a file of around 500-600 MB. Use the file to install Anaconda. Follow the instructions and just install it as a regular software package on Windows. You can follow the detailed instructions [here](https://docs.anaconda.com/free/anaconda/install/windows/). It's important that you *don't add Anaconda to your PATH variable*. This is the default setting during installation, so you should be fine.
#
# ![Anaconda installer](https://docs.anaconda.com/_images/win-install-destination1.png)
#
# Anaconda installs some additional tools on your machine, including Anaconda Navigator. This is a tool that conveniently combines several important elements of your Python distribution: environments, packages. For now, we will not discuss environments too much, but we will do so extensively later in the course.
#
# :::{admonition} Before you continue
# :class: warning
# Before you continue, please make sure that you have successfully installed Anaconda.
# :::

# ## Using the command line
# One useful skill to have as a programmer is to be able to effectively use the command line. The command line is a text interface to your computer. You can use it to - for example - navigate your computer, create and delete files, inspect which processes are happening. The command line also offers an alternative to the graphics user interface (GUI) that you are used to, and you will find that many software tools can be used either via the command line or via a GUI. 
#
# :::{admonition} Terminal? Shell?
# :class: note
# You'll find that the words 'terminal', 'command line', 'shell', 'CLI', 'console', and 'prompt' are all used for the same thing: a text-based interface to your computer.
# :::
#
# To start, open the a terminal window. In Windows, you do this by pressing the Windows key on your keyboard and typing `cmd` in the search window. This should open a command line interface (CLI).
#
# ![terminal](https://surfdrive.surf.nl/files/index.php/s/sKLT3yb3zKhQXj3/download)
#
# There are many things that you can do with the command line, but one essential skill is to be able to navigate your filesystem. As you might be aware, the file system on your computer is organized like a tree, with directories/folders and subdirectories. 
#
# ![filesystem](https://cdn.ttgtmedia.com/rms/onlineImages/TT_tree_mobile.jpg)
#
# The table below provides a couple of common commands that you can use to navigate your file system.
#
# | Command | Example |    |
# |--- |--- |--- |
# |`ls` (short for 'list') | `ls` | List contents (files and subdirectories) of current directory |
# |                        | `ls .\scripts` | List contents subdirectory `scripts` |
# |`cd` (change directory) | `cd ..` | Go one level up in directory structure | 
# |     | `cd .\scripts` | Go to directory `scripts` which is a subdirectory of the current directory |
# |     | `cd C:\Users` | Go directly to a directory by using it's full path on the machine |
#
# :::{admonition} Exercise 1.1
# :class: tip
# 1. Create a Microsoft Word file called `AnswersTutorial1.docx` and save it somewhere in a folder of your choosing. In this week's tutorial, you will use this file to store all your answers.
# 2. Start a terminal window. 
# 3. Use the commands above to navigate to the folder where you stored your `Exercise1.docx` file. Display the contents of that folder. Make a screenshot of the terminal and paste it to your `AnswersTutorial1.docx` file.
# :::
#
#
# ## The Python interpreter
# Python is a programming language, but once you have installed Anaconda, you also have installed a *Python interpreter*. This is a command line tool that allows you to program in *interactive mode*. 
#
# To start the Python interpreter, type `python` in a terminal and hit <kbd>Enter</kbd>. The output should look something like this. 
#
# ```
# Python 3.11.7 | packaged by conda-forge | (main, Dec 23 2023, 14:27:59) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# ```
#
# There is some useful information in this output. In particular, on the left you see the Python version that you're currently using in combination with Anaconda. Like each software tools, there are multiple versions of Python. Versions 3.11 and 3.12 are the newest versions of Python (as of December 2023) and are most likely to be supported in the long run.

# The `>>>` indicates that you're in interactive mode and Python is 'listening'. Anything that you will type here will be parsed, it will be interpreted, and an answer will be returned to you. Let's give it a try! You can use the interpreter as a calculator and perform some simple arithmetic operations. 
#
# :::{admonition} Exercise 1.2
# :class: tip
# Replicate the output below using the Python interpreter. Remember to press <kbd>Enter</kbd> after each line to send your request to the interpreter. Paste the contents of your terminal window into your Word document.
#
#
# :::
#
#

# ```python
# >>> 1+4
# 5
# >>> 8-6
# 2
# >>> 6*7
# 42
# >>> 8/4
# 2.0
# >>> 5--6
# 11
# ```

# Two things in the previous outputs are interesting to note. First, Python automatically interprets the minus sign in front of 6 and gives the correct answer. Second, if we divide 8 by 4, we don't get 2, but we get 2.0. This has to do with the 'type' of the number. Like most programming languages, Python differentiates between integer numbers (such as 1, 2, 3, 4, ..., 100000, ...) and floating point numbers (such as -45.7, 0.00001, 12.9772). By default, if we divide two numbers using `/`, Python returns a floating point number to preserve *precision*.
#
# We can use the interpreter as a calculator. For many standard operations there is a version in Python. The table below gives an overview of some command mathematical operations and how to implement them in Python.
#
# |Mathematical notation | Python |
# |--- | ---|
# |$a+b$ | `a+b` |
# |$a-b$ | `a-b` |
# |$ab$ | `a*b` |
# |$\frac{a}{b}$ | `a/b`|
# |$a^b$ | `a**b` |
# |$a>b$ | `a>b` |
# |$a<b$ | `a<b` |
# |$a\geq b$ | `a>=b` |
# |$a\leq b$ | `a<=b` |
#
#
# If you want to reuse the output of a previous expression, you can use the `_` symbol. For example, to compute $4 * 5 + 6$, we can do
#
# ```python
# >>> 4*5
# 20
# >>> _+6
# 26
# ```
#
# Of course, you can also directly make more complex statements. The use of `(` and `)` can help you properly structure your inputs. The location of the parentheses affects the output of the interpreter, e.g.,
#
# ```python
# >>> 4*5+6
# 26
# >>> 4*(5+6)
# 44
# ```

# :::{admonition} Exercise 1.3
# :class: tip
# Evaluate the following expressions by hand and use Python to check the answers. 
#
# 1. `2/2*3`
# 2. `8*54`
# 3. `8*(54)`
# 4. `7-5*49`
# 5. `6-2/5+7**2-1`
# 6. `10/25-3+2*4`
# 7. `3**2/4`
# 8. `3**2**3`
# 9. `(3**2)**3`
#
# Paste the contents of your terminal window into your Word document.
#
# :::

# ## Variables
# By now, you can use Python as a basic calculator, but this is not yet real programming. You haven't really stored values properly yet, only in the last output `_`, so it's hard to perform more complex computations. One key element of programming is the use of named variables and the ability to store values in those variables.
#
# ```{admonition} Variables
# :class: note
# Variables are containers for storing data values.
# ```
#
# Within the Python interpreter, you can define a variable and assign a value to it. To do so, try something like
#
# ```python
# >>> a=4 
# >>>
# ```
#
# You may notice that now, the interpreter does not return an output value. This is so because it has stored the value 4 in variable `a` and simply storing a value in a variable does not result in an output. However, we can now simply ask the interpreter for the value of `a` and it returns 4. 
#
# ```python
# >>> a
# 4
# ```
#
# As long as the Python interpreter is running, it will remember what the value of variable `a` is. Likewise, we can assign values to other variables.
#
# ```python
# >>> b = 3
# >>> c = 7
# ```
#
# Then, instead of using *values* to perform computations, we can use *variables* instead. For example, we can perform some basic arithmetic with these variables as follows:
#
# ```python
# >>> (a*b)-c
# 5
# ```
#
# Moreover, we can assign the output of such arithmetic to a new variable.
#
# ```python
# >>> d = (a*b)-c
# >>>
# ```
#
# Again, the Python interpreter does not return anything, as we're just assigning a value to `d`. At any moment, you can list all current variables by typing `vars()`.
#
# ```python
# >>> vars()
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 4, 'b': 3, 'c': 7, 'd': 5}
# ```
#
# You can always replace the value of a variable, so you can reuse variable names as much as you want. 
#
# ```python
# >>> d = c**b+a
# >>> d
# 347
# ```
#
# and 
#
# ```python
# >>> vars()
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 4, 'b': 3, 'c': 7, 'd': 347}
# ```
#
# This is also a pitfall! When naming your variables, you should make sure that you're not reusing the name of something that already exists in Python. For example, if you type
#
# ```python
# print = 5
# ```
#
# you will find that you can no longer print output with the `print` function.
#
#
# ```{admonition} Case sensitivity
# :class: warning
# The *case* of your variable name matters. For example, if you first assign a value to a variable that you call `a` and then want to reuse the variable of that variable but (accidentally) type `A`, Python will throw an error:
#
#     >>> a=5
#     >>> b=A*4
#     Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#     NameError: name 'A' is not defined
#
# This could lead to unexpected behavior, in particular when you actually have two variables defined, one with uppercase and one with lowercase formatting. To prevent such problems, it is good to name your variables according to some standards. We'll introduce these later. 
# ```
#
# ### Assigning values to multiple variables
# For clarity, it is often better to use one line of code to assign a value to one variable, but sometimes you may want to assign values to two variables at the same time. In that case, you can simply separate the variables and values by a comma, as in
#
# ```python
# a, b, c = 1, 2, 3
# ```
#
# It is of course important that the number of values matches the numbers of variables. If that is not the case, Python will throw an error.

a, b, c = 1, 2

# You can also assign the *same value* to multiple variables. For example, to create three variables that all have the value `2`, you can simply write
#
# ```python
# a = b = c = 2
# ```
#
# :::{admonition} Exercise 1.4
# :class: tip
# Special numbers like $\pi$ and Euler's number $e$ are not automatically defined in Python. Define these two numbers as variables and use them to compute the volume of a sphere with radius $e$. Store the result in a new variable called `v`. 
#
# Paste the contents of your terminal window into your Word document.
# :::

# ## Data types
# Each variable in Python has a *type* that defines which kind of data it represents. There are four important types in Python that you will also see in almost any programming language:
# 1. Integers, or whole numbers such as 1, 2, 1000, 4000. 
# 2. Floating point numbers such as -1892.3, 0.000045, 1.3040, 9828.322.
# 3. Strings, i.e., sequences of characters. For example, 'Technical medicine' is a string.
# 4. Booleans, i.e., `True` or `False`
#
# Some programming languages require you to specify the type of each variable. Instead, Python tries to automatically infer the type of a variable for you. However, it's always good to be aware of the type of your variables.To find out what the type is of a variable, you can use `type()`, i.e.,
#
# ```python
# >>> a = 4
# >>> type(a)
# <class 'int'>
# >>> b = 3.1
# >>> type(b)
# <class 'float'>
# >>> c = 'Technical medicine'
# >>> type(c)
# <class 'str'>
# >>> d = True
# >>> type(d)
# <class 'bool'>
# ```
#
# Not all data types are compatible. While you can add integers and floating point numbers, and even booleans and numbers, adding floating point and strings will throw an error. 

4 + 'Hello world'

# :::{admonition} Exercise 1.5
# :class: tip
# Define two variables. One should have the value 'Technical ' and the other 'Medicine'. What is the type of these variables? Try to add these two variables in the Python interpreter. Which result do you get? Can you explain what happened?
# :::
#
# Some arithmetic operations take inputs of one type and return outputs of another type. For example, evaluating if one integer is smaller than another integer will return a boolean: the statement is either `True` or `False`. 
#
# ```python
# >>> a < 1
# False
# >>> a > b
# False
# >>> a <= b
# True
# >>> a >= b
# False
# ```

# Special variants of this are the `not`, `or` and `and` operators. These return either `True` or `False` depending on the input. As you might expect, by writing `not` before a statement, we get the opposite value.
#
# ```python
# >>> a = 4
# >>> a < 1
# False
# >>> not a < 1
# True
# ```
#
# With `or` and `and` we can combine two statements. For example
#
# ```python
# >>> a = 4
# >>> b = 3
# >>> a > 2 and b > 1
# True
# >>> a > 2 or b > 4
# True
# ```
#
# And of course, `and` and `or` can also be combined with `not`.
#
# ```python
# >>> not a > 2 or b > 1
# True
# ```
#
# Here, parentheses `()` matter. For example, consider the following output.
#
# ```python 
# >>> not (a > 2 or b > 1)
# True
# ```
#
# :::{admonition} Exercise 1.6
# :class: tip
# For each of the following nonsense programs, write down the expected output and verify in the Python interpreter.
#
# 1. 
# ```python
# a = True
# b = False
# print(not(a))
# print(not(b))
# ```
#
# 2. 
# ```python
# a = False
# b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)
# ```
#
# 3. 
# ```python
# a = False
# b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)
# ```
#
# :::

# ## Complex numbers
# A convenient feature of Python is that it comes with built-in support for complex numbers. You can easily define a complex number as
#
# ```python 
# >>> z = 3 + 2j
# ```
#
# :::{admonition} Literals
# :class: warning
# As you notice, Python uses the literal $j$ instead of $i$ in complex numbers. This is an engineering convention.
# :::
#
# :::{admonition} Exercise 1.7
# :class: tip
# 1. Use the Python interpreter to find out the type of the variable `z`.
# 2. Choose two complex numbers, for example $-3 + 2j$ and $5-7j$. Add, subtract, multiply and divide these numbers in Python.
#
# Paste the contents of your terminal window into your Word document.
# :::
#
#

# ## Tuples, lists, sets, and dictionaries
# In addition to integers, floating point numbers, strings, and booleans, Python has a couple of other very useful data types: tuples, lists, sets and dictionaries. All of these are collections, which can be used to store multiple values or variables. However, there are some important differences between these four data types. The following table from [this website](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/) nicely summarizes the differences between tuples, lists, sets and dictionaries. We'll elaborate below.
# | Tuple                                                                                                              | List                                                                                                             | Set                                                                                                      | Dictionary                                                                         |
# |--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
# | A Tuple is also a non-homogeneous data structure that stores elements in columns of a single row or multiple rows. | A list is a non-homogeneous data structure that stores the elements in columns of a single row or multiple rows. | The set data structure is also a non-homogeneous data structure but stores the elements in a single row. | A dictionary is also a non-homogeneous data structure that stores key-value pairs. |
# |                                          Tuple can be represented by  ( )                                          |                                        The list can be represented by [ ]                                        |                                     The set can be represented by { }                                    |                      The dictionary can be represented by { }                      |
# |                                           Tuple allows duplicate elements                                          |                                        The list allows duplicate elements                                        |                                 The Set will not allow duplicate elements                                |                    The dictionary doesn’t allow duplicate keys.                    |
# |                                           Tuple can use nested among all                                           |                                         The list can use nested among all                                        |                                     The set can use nested among all                                     |                       The dictionary can use nested among all                      |
# |                                              Example: `(1, 2, 3, 4, 5)`                                              |                                             Example: `[1, 2, 3, 4, 5]`                                             |                                         Example: `{1, 2, 3, 4, 5}`                                         |                  Example: `{1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}`                 |
# |                                  Tuple can be created using the tuple() function.                                  |                                  A list can be created using the list() function                                 |                         A set can be created using the set() function                        |               A dictionary can be created using the dict() function.               |
# |                         A tuple is immutable i.e we can not make any changes in the tuple.                         |                            A list is mutable i.e we can make any changes in the list.                            |         A set is mutable i.e we can make any changes in the set, ut elements are not duplicated.         |                A dictionary is mutable, ut Keys are not duplicated.                |
# |                                                  Tuple is ordered                                                  |                                                  List is ordered                                                 |                                             Set is unordered                                             |                    Dictionary is ordered (Python 3.7 and above)                    |
# |                                            Creating an empty Tuple t=()                                            |                                            Creating an empty list l=[]                                           |                                      Creating a set a=set() b=set(a)                                     |                          Creating an empty dictionary d={}                         |
#
# ### Tuple
# We define a tuple in Python using parentheses `()`. For example, we can define a tuple with three items as follows.
#
# ```python
# >>> a = (3, 5, 4)
# ```
#
# A tuple has two properties: it is ordered and it is unchangeable.  This means that the values with which we initialize the tuple stay in their order (even if they are not ascending or descending, or alphabetically ordered), and we cannot change individual values. We can access the value of the individual items in the tuple using `[]`. For example, to get the value of the **first** element in the tuple, we use the *index* of that element in `a` and write 
#
# ```python
# >>> a[0]
# 3
# ```
#
# ```{warning}
# Note that to get the **first** element, we use index 0. In most programming languages, we start counting at 0, and not at 1 (as you might expect and are probably used to doing).
# ```
#
# The second property of the tuple is that it is **unchangeable**. Hence, we cannot change the values of its individual elements, or *assign* a value to one of the elements. Let's give that a try below. Indeed, we get an error. Take a close look at this error, it tells you exactly what the problem is: tuples do not allow item assignment.
#
# ```python
# >>> a[0] = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# ```

# ### List
# Like a tuple, a list can contain multiple items. Similarly to a tuple, these are ordered. Different than in a tuple, they are also changeable. A list is defined using square brackets `[]`. 
#
# ```python
# >>> a = [3, 5, 4]
# >>> a
# [3, 5, 4]
# ```
#
# To illustrate what we mean with *changeable*, let's assign a new value to the second element
#
# ```python
# >>> a[1] = 6
# >>> a
# [3, 6, 4]
# ```
#
# Note how we don't get an error in this case. Also, the order stays the same. Moreover, the list length is dynamic: given the list `a`, we can combine add another list to it.
#
# ```python
# >>> a = a + [7, 9]
# >>> a
# [3, 6, 4, 6]
# ```
# To add *one* item at the end of a list, we can use the `append` method as follows
#
# ```python
# >>> a = [3, 5, 4]
# >>> a.append(7)
# >>> a
# [3, 5, 4, 7]
# ```
#
# To add *multiple* items to the end of a list, we can use the `extend` method
#
# ```python
# >>> a = [3, 5, 4]
# >>> a.extend([6, 7])
# >>> a
# [3, 5, 4, 6, 7]
# ```
#
# There are two ways to remove items from a list. First, the `pop` method removes an item from a list at a given index and returns its value. Second, the `remove` method removes an item based on its value. The code below demonstrates this.
#
# ```python
# >>> a = ['apple', 'banana', 'cherry']
# >>> a.pop(1)
# 'banana'
# >>> a.remove('cherry')
# >>> a
# ['apple']
# ```
#
# Each item in a list (or tuple) can have its own data type. We can make lists consisting of integers, strings, or combinations of these.
#
# ```python
# >>> a = ['apple', 'banana', 'cherry']
# >>> b = [3, 5, 4]
# >>> c = ['apple', 5, '3']
# >>> a
# ['apple', 'banana', 'cherry']
# >>> b
# [3, 5, 4]
# >>> c
# ['apple', 5, '3']
# ```
#
# We can *index* a list using integer numbers in square brackets (e.g, `a[1]` returns 'banana'), and we can also index by counting back from the last element by using negative integer numbers, where index -1 refers to the last item, -2 to the second-to-last item, etc. This means that - in this example - `a[0]` and `a[-3]` should result in the same value.
#
# :::{admonition} Exercise 1.8
# :class: tip
# Why do `a[0]` and `a[-3]` refer to the same value?
# :::
#
# In addition to *indexing* a list, we can also *slice* a list. This means that we select a portion of the list based on a start and an end index. In the example below, we select all items starting at index 3 and until (but not including) index 5.  
#
# ```python
# >>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# >>> a[3:5]
# ['tomato', 'ham']
# ```
#
# If the start and end index are not defined, we are simply selecting all items in the list
#
# ```python
# >>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# >>> a[:]
# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# ```
#
# We can also slice by adding an increment (in this case 2). This only selects every second (in this case) element. 
#
# ```python
# >>> a[2:6:2]
# ['bacon', 'ham']
# ```
#
# We can reverse the order in a list by not defining the start and end, and making the increment negative. In this case, the slicing starts at the end of the list.
#
# ```python
# >>> a[::-1]
# ['lobster', 'ham', 'tomato', 'bacon', 'egg', 'spam']
# ```
#
# Items in a list can even be variables, and lists can contain other lists. By nesting your indices, you can access the individual items in the *nested* lists.
#
# ```python
# >>> c[2] = a
# >>> c
# ['apple', 5, ['lobster', 'ham', 'tomato', 'bacon', 'egg', 'spam']]
# >>> c[2][2]
# 'tomato'
# ```
#
# ```{note}
# Indexing and slicing work the same way for lists and tuples.
# ```

# ### Set 
# A set is a collection that is unordered and does not allow duplicate values. Sets cannot contain multiple items with the same value. Sets are defined using curly brackets `{}`. In the example below, you can note two things
# 1. Although we assign two `5`s to the set, the set only contains one `5`. The reason for this is that a set does not allow duplicate values.
# 2. Although the `4` comes after the `5` in our assignment, the order is swapped to be increasing in the eventual set. This is the case because a set is not ordered: elements will be sorted in increasing order by design.
#
#
# ```
# >>> a = {3, 5, 5, 4}
# >>> a
# {3, 4, 5}
# ```
#
# You will find that sets can be very useful when you want to perform common mathematical operations like unions and intersections. Sets have some built-in *functions* that allow you do this. For example, if we have two groups of people, we can use sets for boolean operators.
#
# ```python
# >>> a = {'Adam', 'Bob', 'Claire', 'Dean'}
# >>> b = {'Bob', 'Dean', 'Edward', 'Fran'}
# >>> a.intersection(b)      # Who is in both groups (intersection)
# {'Dean', 'Bob'}
# >>> a.union(b)             # All people (union)
# {'Dean', 'Fran', 'Bob', 'Claire', 'Adam', 'Edward'}
# >>> a.difference(b)        # Everyone that is in one group, minus those people that are also in another group
# {'Adam', 'Claire'}
# ```
#
# Just like in tuples, you cannot assign values to indices in sets. However, you can add and remove elements from sets using the `add` and `remove` functions, as follows.
#
# ```python
# >>> a = {'Adam', 'Bob', 'Claire', 'Dean'}
# >>> a.add('Edward')
# >>> a
# {'Dean', 'Bob', 'Claire', 'Adam', 'Edward'}
# >>> a.remove('Bob')
# >>> a
# {'Dean', 'Claire', 'Adam', 'Edward'}
# ```

# ### Dictionary
# A dictionary is a collection that contains items which are pairs of keys and values. As with lists, tuples and sets, a dictionary can contain items with different data types. Keys do not necessarily have a specific type, and neither do values. Dictionaries ar defined using curly brackets `{}` and keys and values are separated using a colon `:`.
#
# ```python
# >>> car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# >>> car
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# ```
#
# :::{admonition} Single or double quotes
# :class: note
# Some programming languages distinguish between using 'single quotes' and "double quotes", but Python does not. You're free to choose what you prefer. As you can see above, even if you use double quotes, Python will turn these into single quotes.
# :::
#
# Dictionaries are very useful in many applications that you will see during this course. Note that we cannot use indexing and slicing in dictionaries, but we can get values in dictionaries by using keys. For example, if the dictionary above defines a car, we can use `car["brand"]` to get the brand of this car.
#
# ```python
# >>> car['brand']
# 'Ford'
# ```
#
# If you want to add something to an existing dictionary, you can simply assign a new key and value pair as follows
#
# ```python
# >>> car['color'] = 'Blue'
# >>> car
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'Blue'}
# ```
#
# And to remove something, you can use `del` as follows
#
# ```python
# >>> del car['model']
# >>> car
# {'brand': 'Ford', 'year': 1964, 'color': 'Blue'}
# ```
#
# Note that dictionary keys and values can have any type. They don't have to be strings or integers. This makes dictionaries very flexible and useful in practice. However, there are some restrictions that you should keep in mind:
# 1. A key can only appears in a dictionary once, duplicate keys are not allowed. 
# 2. If you assign a new value to a key, it overwrites the old value.

# ### Converting between collections
# If your data is organized in a set, you can turn it into a list or vice versa. However, keep in mind the characteristics of these data types. For example, if you have a list with *duplicate* values and you turn that into a set, you'll lose the duplicates. This *can* be convenient, for example if you want to automatically select all unique values in a list. In the code below, notice how the set contains all unique elements in the list, ordered in ascending order, while the tuple maintains the original order and preserves duplicates.
#
# ```python
# >>> a = [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5]
# >>> set(a)
# {1, 2, 3, 4, 5}
# >>> tuple(a)
# (1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5)
# ```
#
# Dictionaries cannot be directly transformed into lists or sets, but you can get a list of either the keys or values in a dictionary using the `keys()` and `values()` methods
#
# ```python
# >>> car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# >>> list(car.keys())
# ['brand', 'model', 'year']
# >>> list(car.values())
# ['Ford', 'Mustang', 1964]
# ```
#
# To create a new dictionary from two lists (one containing keys, one values), use the `zip` function. This function takes two lists and, like a zipper, loops over pairs of items in both lists. Each pair is combined in a tuple, and a new list is made using all these tuples. Using the `dict` function, this list can be turned into a dictionary. The following code illustrates this.
#
# ```python
# >>> keys = ['brand', 'model', 'year']
# >>> values = ['Ford', 'Mustang', 1964]
# >>> list(zip(keys, values))
# [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]
# >>> dict(_)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# ```
#
# And voilà, we have retrieved our original dictionary.
#

# :::{admonition} Exercise 1.9
# :class: tip
# 1. Reverse the order of tuple `t = (10, 20, 30, 40, 50)`
# 2. Given list `l = [10, 20, 30, 40, 'a', 'dog', 3.4, True]`, make two new lists: one containing every second item counting from the back, and one containing every third item. 
# 3. Given tuple `t = ("Orange", [10, 20, 30], (5, 15, 25))`, write a line of Python code to extract the value 
# 4. Use slicing to get a tuple `t2 = (44, 55)` from tuple `t1 = (11, 22, 33, 44, 55, 66)`.
# 5. Given the below dictionary, write a line of code that outputs Mike's grade for history. 
# ```python
# {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "grades": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# ```
#
# 6. Given the below dictionary, raise the salary of Brad to 6800.
# ```python
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
#
# ```
# 7. Define a dictionary called `student` that contains your own name, hair color, and age.
# 8. Create a list containing yourself and two additional students as dictionaries.
#
# Paste the contents of your terminal window into your Word document.
# :::

# ## The `in` operator
# For tuples, lists, sets, and dictionaries, Python provides the `in` operator, which checks whether a value is present in the collection. If so, it returns `True`, if not it returns `False`.
#
# ```python
# >>> a = [1, 2, 3, 4]
# >>> 1 in a
# True
# >>> a = {1, 2, 3, 4}
# >>> 1 in a
# True
# >>> a = (1, 2, 3, 4)
# >>> 1 in a
# True
# >>> a = {1: 4, 2: 5}
# >>> 1 in a
# True
# ```
#
# This operator can also be easily combined with `not` to ask for the opposite response. Consider the following examples.
#
# ```python
# >>> car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# >>> 'brand' not in car
# False
# ```
#
# As you will see in the next chapter, this is useful to define expressions regarding containers.
