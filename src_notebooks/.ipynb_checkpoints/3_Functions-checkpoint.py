# # Functions
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * define a function in Python
# * understand the concept of scope, local and global variables
# * create a function with one or more input arguments and one or more output arguments
# * understand what recursion is and know when to use it and when not
# * provide arguments to a script
# * how to format output strings
# * use Jupyter notebooks
# :::
#
#
# By now you can write and run a Python script, you can write conditional statements using `if`, `elif` and `else`, and you can write `for` and `while` loops. You have written scripts that can be called with *arguments* that dynamically define the output of the script. In Python, if we want to repeatedly do something but the output depends on some input, we are going to need **functions**. In Python, functions are everywhere. In fact, you have already used functions: for example, the `print()` function outputs something to the screen. Depending on what we call it with, our output is different.
#
# ```python
# >>> print('Hello')
# Hello
# >>> print('Bonjour')
# Bonjour
# ```
#
# You can think of a function as a mini-program that runs within another program or within another function. The main program calls the mini-program and sends information that the mini-program will need as it runs. When the function completes all of its actions, it may send some data back to the main program that has called it. The primary purpose of a function is to allow you to reuse the code within it whenever you need it, using different inputs if required.
#
# When you use functions, you are extending your Python vocabulary. This lets you express the solution to your problem in a clearer and more succinct way.
#
# In Python, by convention, you should name a function using lowercase letters with words separated by an underscore, such as `do_something()`. These conventions are described in PEP 8, which is Python’s style guide. You’ll need to add parentheses after the function name when you call it. Since functions represent actions, it’s a best practice to start your function names with a verb to make your code more readable.
#
# ## A very basic function
# Let's start by considering a scenario in which we have a piece of code that we repeatedly need to execute. Let's start by creating a very basic function. For some reason, we're writing a program in which we repeatedly want to do the following 
#
# ```python
# for a in [1, 2, 3, 4, 5, 6]:
#     for b in [1, 3, 5]:
#         print(a**b)
# ```
#
# We can put this block of code in a function
#
# ```python
# def useless_power():
#     for a in [1, 2, 3, 4, 5, 6]:
#         for b in [1, 3, 5]:
#             print(a**b)
# ```
#
# ## Functions with arguments
# Things get more interesting if our function does no exactly the same whenever it is called, but actually changes its output depending on the input that we provide. For example, we can write a function that computed the 
#
# ```python
#
# ```
#
# The function has *parameters*, and we pass *arguments* as the values to those parameters. 
#
# :::{admonition}
# :class: tip
# Consider the banking Exercise 2.3. Write a function that takes in a customers age and annual income and returns the required answer.
# :::
#
#
# ## Optional arguments 
# Python differentiates between *required* and *optional* arguments. Required arguments *should* always be provided to the function. If they are not provided, Python throws an error. Optional arguments *could* be provided, but when they are not provided, the function still runs. This is because we provide *default* parameter values: if the user does not provide other values, these are used. Consider the following example:
#
#
# Because it can be confusing which argument refers to which parameter, you should provide names if there are multiple optional arguments. These are referred to as keyword arguments.
#
# ## Return 
# A function can return a value that it has computed. This is useful if we want to compute. Return one value or multiple values, what happens with `_`. 
#
#
# ## Scope
# Each variable in Python has a `scope`, which is either local or global.
#
#
# ```python
# x = 4
#
# def some_function(x):
#     print(x)
#     
# some_function(10)
# print(x)
# ```
#
# The `x` variable in `some_function` only has a local scope and does not override the global variable `x`.
#
#
#
# ## The anatomy of a Python function
# Python functions can have very different tasks, but each 
#
#
#
# ## Recursive functions
# We can call functions from anywhere, and we can even call a function from within itself. This is called a *recursive* function. A famous example is the factorial $n!$. We can implement this in a function as
#
# ```python
# def factorial(n):
#     if n > 0:
#         return n * factorial(n-1)
#     else:
#         return 1
# ```
#
# :::{admonition} Exercise
# :class: tip
# Try and write out for yourself what happens when we call `factorial(4)`. What is the order in which lines are executed, and what is the answer that the function gives?
# :::
#
# In practice, you won't encounter many recursive functions, but it's good to be aware that in principle, there is no reason why a function cannot be called from within itself.
#
# ## STILL ADD ARGS AND KWARGS??
#
# :::{admonition} Exercise
# :class: tip
# In this exercise, you're going to write your own functions.
#
# TODO
#
# :::

# ## Built-in functions
# You don't have to define each function yourself: Python has a number of built-in functions that are available in any Python distribution. Useful functions include the `len` function and the `print` function that you have already used. In addition to the functions that you can write yourself, Python has a number of *built-in* functions. These are functions that are always available if you program in Python. Examples are `print()`. A complete list of built-in functions is available [here](https://docs.python.org/3/library/functions.html). Take a look, you'll likely recognize some of them. We have previously used the `round()` and `range()` functions, and it's clear what - for example - the `abs()` does. Likewise, you have used the `type()` function to find out what the type of a variable is.
#

# ## Jupyter notebooks
# By now, you have programmed in the command line using the interpreter and you have written and ran scripts. Now we're going to teach you a *third* and very popular way to program in Python: using notebooks. A Jupyter notebook is a file with `.ipynb` extension that can contain code as well as text or *Markdown*. The notebook consists of *cells* and each cell can be *ran* by a Python *kernel* that is running in the background. This Python **kernel** is a lot like the interpreter you have been using interactively.
#
# ### Cells
# There are three types of cells in notebooks
# 1. **Code cells**. These are cells that can be run and interpreted by Python
# 2. **Markdown cells**. These are cells that contain text in the *Markdown* style. Markdown is a bit like LaTeX.
#
#
# ### How to run notebooks
# There are multiple ways to run Jupyter notebooks
# 1. In VS Code using an extension
# 2. Run locally on your computer in the browser
# 3. Not locally on your computer, but on the University of Twente server: `jupyter.utwente.nl`
# 4. Google offers Google Colab, which is a lot like Jupyter Notebooks and is (almost) fully compatible
#
# All of these are valid options, you might want to use option (1) to stay in VS Code, of if you'd rather work in your browser, you can use option (2).
#
# ### Starting a notebook server
# Navigate to the directory in which you want to work, go to the command line and type `jupyter lab`.
#
# In fact, this whole book is made out of Jupyter notebooks! You can download each chapter as an `*.ipynb` file and run it as a notebook.
#
# :::{admonition} Exercises 
# :class: warning
# From the next chapter on, you will be asked to write all exercises in a notebook instead of in a `*.py` script.
# :::
#
# ### The kernel
#
#
#
# ### Command line
# When inside a Jupyter notebook, you can run things on the command line using the `!` command. For example, to list the contents of the current directory, you can run `!dir` (on Windows) or `!ls` (on Mac and Linux). This is also convenient when you're working in a notebook and you want to install a missing package. You can then run - for example - `!conda install <package_name>` without first having to go to the terminal.

# !ls

# ### The `main` function
# When you run a complex Python script, you don't want to run all the lines sequentially, but you want to indicate the interpreter where to *enter* your code. By design, this is the `main` function. The `if`-statement at the bottom is used to make sure that when you import a script into another script (more about that later) Python doesn't execute the full file.
#
# ```python
# def main():
#     print("Python main function")
#
#
# if __name__ == '__main__':
#     main()
# ```


