# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] user_expressions=[]
# # Writing scripts
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * execute a Python script
# * write a Python script using Visual Studio Code
# * use if, elif, and else
# * write while loops 
# * write for loops
# :::
#
# Last week, you have used the Python interpreter to interact with Python. As you can imagine, once you want to write and run a piece of code that contains many steps, it becomes inconvenient to use the interpreter: you would have to write each line of code each time you're trying to run a oprogram. Instead, you can write Python *scripts* that can be passed to the interpreter, which will run everything line-by-line. Python scripts are files that can be *run* and are supposed to do something each time you run them. In practice, a Python file is a file whose name ends in `.py`, and can be simply a set of statements. For example, following what you did last week, the contents of a Python file can be

# + [markdown] user_expressions=[]
# ```python
# a = ['cat', 'dog', 324, 8.14, ['house', 'enschede', 4]]
# print(a[2:4])     # print(*) allows you two print something back to the command line
# ```

# + [markdown] user_expressions=[]
# You can see that these are just two lines of code, which should more or less similar. The first line defines variable `a` as a list of items, including another list. The second line *slices* this list and prints these items. 
#
# In the second line, we have also added a *comment*. This is a piece of human-readable text that is not part of the code. It will not be run by the Python interpreter. We use the character `#` to indicate that this is a comment. Documenting your code properly with comments is a very valuable way to make sure that you (or someone else) will still understand the code when you look at it later. We'll go over some common practices for code documentation later.
#
# Running a Python script can be straightforward. First, you have to actually create the script. Make a directory/folder on your computer where you intend to store the code of this course. This can be the same directory where you stored the Word file of the previous chapter. Open Notepad (*Kladblok*) and paste these two lines of code. Then go to `File` -> `Save as`, under `Save as type` select `All files` and save the file as `test.py` in the directory you just created. Then, open a command line window and do one of the following
# 1. Navigate to the directory where you have stored `test.py` and run `python test.py`
# 2. Directly run `python {directory}\test.py`, where you replace `{directory}` with the directory where you stored the file.
#
# ```{admonition} Exercise 2.1
# :class: tip
# 1. What is the output of this script?
# 2. Change and run the script so that the output is ['house', 'enschede']
# 3. Turn the list into a tuple. What is the output? 
# ```

# + [markdown] user_expressions=[]
# And that's it: you've written and run your first Python script! Now we can really start programming. There is no limit to how long a script can be and - as you'll see - you can do much more in a script than just processing lines in a fixed order. 

# + [markdown] user_expressions=[]
# ## Visual Studio Code
# For simple programming, Notepad will get you quite far as a script editor. However, most programmers use an 'integrated development environment' (IDE) that provides additional tools during programming to increase productivity and help you write clear and reusable code. There are many different IDEs on the market, some focusing on one programming language, one on a range of programming languages. Some are very expensive and intended for professional use, some are free. Some are complex, some are easier to use. In this course, **we will use Visual Studio Code**, commonly referred to as VS Code. VS Code is free, flexible, and widely considered to be a good entry point for new programmers. In the remainder of the course, we assume that you are using VS Code.
#
# To install VS Code, take the following steps:
# 1. Go to [the Visual Studio Code website](https://code.visualstudio.com/download) and download the correct version for your computer. If you're on a Windows laptop, this is likely going to be the *User Installer* `x64` version.
# 2. Run the installer to install Visual Studio Code.
# 3. Open Visual Studio Code and go to 'Extensions' (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd> on Windows).
# 4. Install the Python extension. **Warning** There are multiple Python extensions available. You should download the most popular one by Microsoft, which has been downloaded over a 100m times.
#
# If you have properly installed Anaconda as described in the previous chapter, you should now be able to use Python within the VS Code IDE. You can find more information on the combination of Anaconda and VS Code on the [Anaconda website](https://docs.anaconda.com/free/anaconda/ide-tutorials/python-vsc/).
#
# It's good to be aware that there are other (free) IDEs that you can also use, like Spyder and PyCharm. The latter is a professional, expensive IDE that provides free licenses to students. Go to [the JetBrains website](https://www.jetbrains.com/shop/eform/students) and register as a student. Make sure to use  your University of Twente email account. Once you have received confirmation from JetBrains, download the latest version of PyCharm from [the PyCharm website](https://www.jetbrains.com/pycharm/). Use the license provides to you by JetBrains. 
#
#
# ## Writing scripts in VS Code
# Writing code is all about keeping your files organized. With VS Code open, go to the 'Explorer' (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> on Windows). Go to `File` --> `Open Folder` and select the folder you just created and in which you stored `test.py`. If all is well, you should see the folder appear in 'Explorer', including the `test.py` file. You can double click on the `test.py` file and it will open in the VS Code editor. You will see that many colors are used to highlight individual words and characters in the code. This is called *syntax highlighting* and is a useful tool to make your code readable and easily spot errors. You can change the colors and the general look-and-feel of VS Code by picking a different theme. For this, go to `File` --> `Preferences` --> `Theme` --> `Color Theme`. Note that this is just a visualization and will not change anything to your code or what your code does. The editor in which you now see your code is basically a text editor with some nice additional functionality to make your life as a programmer easier.
#
# :::{admonition} Exercise 2.2
# :class: tip
# Extend your Python script as follows:
# 1. Define a variable `b = [4, 5, 6]`.
# 2. Define a new variable `c` that sums the second and third element of `b`.
# 3. Use `print` to print the value of `c`.
# :::
#
#
# ### Running scripts in VS Code
# There are two ways to run scripts from within VS Code. The first option is very similar to what you did before. From within VS Code, you can open a command line interface, similar to the one you used in the previous chapter. To do so, select `Terminal` --> `New Terminal` from the menu. A command line interface should open at the bottom of your screen. If all is well, you should already be in the same directory as the `test.py` file that you created. Verify this using the `ls` command that you learned in the previous chapter. Now, type `python` in the terminal and verify that you are using your Anaconda distribution. Next, you can, just as in the standard Windows command line interface, type `python test.py` to run your Python script.
#
# The second option basically simplifies this process for you. If you go select `Run` --> `Run Without Debugging` from the menu, VS Code will start a terminal, call the Python interpreter with your script, and output the results in a terminal window.
# -

# ## Conditional statements
# Now that you are able to write and run scripts in VS Code, it is time to do some more interesting programming. So far, your scripts have been quite predictable. They are a series of statements that are executed from top to bottom, i.e., sequential execution. One nice feature of almost all programming languages is that they allow the use of *control structures* that direct the execution of your program. One of the most commonly used control structures is the conditional statement `if`. An `if` statement looks like this:
#
# ```python
# if <expr>:
#     <statement>
# ```
#
# Here, `<expr>` is a *boolean* expression, i.e., something that takes on the value `True` or `False`. The `<statement>` is a valid Python statement, something that will be executed if `<expr>` evaluates to `True`. The colon `:` is part of the Python syntax and should always be placed after the boolean expression. Further, note that there is some whitespace in front of the `<statement>`. This is called *indentation* and is also part of the Python syntax. Python always uses four spaces as indentation. You usually don't have to care of this yourself: the interpreter and any IDE that knows that you're programming in Python will help you automatically use that indentation when necessary. 
#
# To get a better feeling about the behavior of the `if`-statement, take a good look at the following code. Note that the interpreter only prints `yes` if the `<expr>` is `True`. Otherwise, nothing happens. Also, note that `if y` gets evaluated to `True`. This is so because the value of `y` is larger than zero. The `or` in `x or y` does exactly what you expect it to do: it will evaluate to `True` if either of the two expressions that it connects is `True`. In contrast, for the `x and y` statement to be `True`, both `x` and `y` should evaluate to `True`, which is here not the case.
#
# ```python
# >>> x = 0
# >>> y = 5
#
# >>> if x < y:                            # True
# ...     print('yes')
# ...
# yes
# >>> if y < x:                            # False
# ...     print('yes')
# ...
#
# >>> if x:                                # False
# ...     print('yes')
# ...
# >>> if y:                                # True
# ...     print('yes')
# ...
# yes
#
# >>> if x or y:                           # True
# ...     print('yes')
# ...
# yes
# >>> if x and y:                          # False
# ...     print('yes')
# ...
# ```
#
# :::{admonition} Exercise 2.3
# :class: tip
# A bank will offer a customer a loan if they are 21 or over and have an annual income of at least €21000. Write a Python script that defines the customers age and income in a dictionary. Depending on the age and income, one of the following lines should be printed (using the `print` function): 
# - 'We are able to offer you a loan.'
# - 'Unfortunately at this time we are unable to offer you a loan.
# :::

# + [markdown] user_expressions=[]
# ## Blocks
# The `<statement>` that follows an `if` condition in Python doesn't necessarily have to be just one line of code. In fact, you can add a *block* of statements after your `if` condition. As long as you stay at the same indentation level, these will be jointly executed with the first statement. For example, based on the cases above, we could have the following piece of code:
#
# ```python
# if y: 
#     print('y')
#     print('is a positive integer')
#     print('so I will print')
#     print('yes')
# ```
#
# Here, all the print statements form a block of code at the same indentation level. Within a block, you can have additional if statements. For example, instead of writing `if x and y:` as we did above, you could also write the following to get the exact same behavior. Notice that now we have added two levels of indentation.
#
# ```python
# if x:
#     if y:
#         print('yes')
# ```
#
# Blocks can be nested to arbitrary depth, and depending on the expressions, some lines will be executed while others won't. In Python, a block is sometimes called a *suite*.
#
# :::{admonition} Exercise 2.4
# :class: tip 
# One of the lines in the following block of code is **not** executed. Which line is it?
#
# ```python
# if 'foo' in ['foo', 'bar', 'baz']:       
#     print('Outer condition is true')      
#
#     if 10 > 20:                           
#         print('Inner condition 1')        
#
#     print('Between inner conditions')     
#
#     if 10 < 20:                           
#         print('Inner condition 2')        
#
#     print('End of outer condition')       
# print('After outer condition')            
# ```
# :::

# + [markdown] tags=["teacher"] user_expressions=[]
# **Answer**
# The line `print('Inner condition 1')` is not executed because `10 > 20` is `False`.  

# + [markdown] user_expressions=[]
# ## `else` and `elif`
# As you might expect, where there's an `if` there can also be an `else`. This `else` is an expression which is evaluated as the opposite of the `if` expression. The statement following this expression is what gets executed if the expression following `if` is evaluated to be `False`. 
#
# For example, take the following piece of code. In this case, the expression following `if` is obviously `False`, so the statement following `else` will be executed. 
#
# ```python
# if 10 > 20:
#     print('larger')
# else:
#     print('smaller')
# ```
#
# A third kind of expression is the `elif` or 'else if' expression that can be used in case options are not binary. Following an `if` expression, you can have any number of `elif` expressions that you desire, potentially followed by an `else` statement. Note that if the expression following `if` is `True`, none of the other expressions will actually be checked. The following provides an example of using `if`, `elif` and `else`.
#
# ```python
# if language == 'english':
#     print('hello')
# elif language == 'dutch':
#     print('hallo')
# elif language == 'french':
#     print('bonjour')
# else:
#     print('unknown language')
# ```

# + [markdown] user_expressions=[]
# :::{admonition} Exercise 2.5
# :class: tip
# Here an exercise about else and elif
# BASE IT ON EXERCISE 5.7 IN THE MATLAB MANUAL
#
# :::

# + [markdown] user_expressions=[]
# ## Advanced: conditional expression
# In addition to the syntax above, Python offers a compact way of writing binary `if`/`else` statements. This is called a *conditional expression* or *ternary operator* and means that the expression
#
# ```python
# if 10 > 20:
#     print('larger')
# else:
#     print('smaller')
# ```
#
# can also be written in one line of code as 
#
# ```python
# print('larger') if 10 > 20 else print('snaller')
# ```
#
# It can in some cases be useful two write expressions like this, for example when you want to compactly assign a value to a variable. 
#
# ```python
# coat = 'raincoat' if raining else 'jacket'
# ```

# + [markdown] user_expressions=[]
# ## Loops
# Iteration control structures, loops, are used to repeat a block of statements until some condition is
# met. Two types of loops exist: the for-loop and the while-loop.
#
# ### `while` loops
# A while loop executes some statement as long as a condition is `True`. As soon as the condition is `False` the loop will stop iterating. In a `for`-loop the number of iterations is fixed upon entering the loop. 

# + [markdown] user_expressions=[]
# ```python
# n= 100
# k = 0
# while k < N:
#     k = k + 1
#     print(k)
# ```

# + [markdown] user_expressions=[]
# The animation below nicely visualizes how a `while` loop works.

# + [markdown] user_expressions=[]
# ![whileloop](https://surfdrive.surf.nl/files/index.php/s/HdTrPmqyiJpPFjr/download)

# + [markdown] user_expressions=[]
# :::{admonition} Exercise 2.6
# :class: tip
# Exercise about `while` loops
# 1. Write a script that determines the largest integer $n$ for which $\sqrt{1^3} + \sqrt{1^3} + \ldots + \sqrt{n^3}$ is less than 1000.
# :::


# + [markdown] user_expressions=[]
#
#
# ### `for` loops
# The for-loop repeats a group of statements a fixed number of times. The standard for-loop has
# general syntax
#
# ```python
# for item in list/set/tuple/dictionary:
#     do something with item
# ```
#      
# For example, we can print all elements in the list `[1, 2, 3, 5, 8]` as follows
#
# ```python
# for item in [1, 2, 3, 5, 8]:
#     print(item) 
# ```
#
# The for-loop iterates over something which we call an *iterable*: an object that is able to return its items one-by-one. Some iterables are very handy. For example, if we want to print 'Hello world' ten times, we can write 
#
# ```python
# for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print('Hello world')
# ```
#     
# but you can imagine that this becomes challenging if we want to do this 1000 times. The built-in `range(start, stop, step)` function in Python returns an iterable that provides numbers from `start` to `stop` with an interval of `step`. Now, to print 'Hello world' 1000 times, we simply use 
#
# ```python
# for item in range(0, 1000, 1): 
#     print('Hello world')
# ```
#
# In practice, we just write `range(0, 1000, 1)` as `range(1000)` when counting from zero with a step size of 1, the default option.

# + [markdown] user_expressions=[]
# :::{admonition} Exercise 2.7
# :class: tip
# 1. Determine the sum of the first 50 squared numbers with a loop.
# :::
#
# :::{admonition} Exercise
# :class: ip
# Use a loop construction to carry out the computations. Write short scripts
# 1. Create a script with just one loop that calculates the sum of all entries of a vector $x$ and also the vector of running sums. (The running sum of a vector $x$ of $n$ entries is the vector of $n$ entries defined as $[x_0, x_0+x_1, x_0+x_1+x_2, \cdots, x_0+x_1+\ldots+x_n]$. Test your code for x = $[1, 9, 1, 0, 4]$.
# :::
# -
# ## Interactive scripts
# A Python script will run 'as is', i.e., its output is entirely defined by what we put in the script. We can also make the script more interactive by using the `input()` function in Python. This asks the user for an input and stores it in a variable.
#
# ```python
# >>> name = input("Please enter your name: ")
# Please enter your name: Adam
# >>> name
# 'Adam'
# ```


# :::{admonition} Exercise 2.X
# :class: tip
# Adapt the script that you wrote in Exercise 2.5 to request the annual income and age of the customer using the `input` function.
# :::

# Another option to make your scripts depend on user input is to provide *arguments* to the script. The easiest way to do this is using the `sys` package. Each time a Python script is called, it is called with a list of arguments. The first item in the list is always the name of the script, the second item is the first argument, etc. This means that we can *call* a script with some arguments that define its output. In a very simple case, let's say that we have a script called `add.py` and its contents are 
#
# ```python 
# import sys
#
# print(int(sys.argv[1]) + int(sys.argv[2]))
# ```
#
# Then we can simply call this script from the command line with two different numbers and we always get the addition of these numbers in return.
#
# ```bash
# (base) % python add.py 4 5
# 9
# (base) % python add.py 23 54
# 77
# ```

# :::{admonition} Exercise 2.X
# :class: tip
# Adapt the script you wrote earlier one last time so that it can be called with two different arguments: the age of the customer and his annual income.
# :::


