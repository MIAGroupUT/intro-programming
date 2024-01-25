# # NumPy
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * work with vectors and matrices
# * do simple linear algebra
# :::
#
# ##  Vectors and matrices
# For many practical programming problems, you'll need vectors and matrices, or *arrays*. The most common way to work with such objects in Python is using the NumPy package. NumPy is the workhorse for anything related to vectors and matrices and offers functions beyond your wildest dreams. Moreover, many other packages in Python are able to use NumPy arrays. Among these the one-dimensional arrays (aka vectors) and two-dimensional arrays (aka matrices) and numbers are the most common.
#
# ## Importing NumPy
# NumPy is a Python package that needs to be imported in order for you to use it. To import NumPy, just write ```import numpy as np``` at the top of your script. Note that here we are importing the NumPy library with an alias `np`. 
#
# ## Arrays
# Numpy uses objects called *arrays* to store 1D, 2D, 3D, nD data. It's important to realize that it doesn't matter if you have a 1D vector, a 2D matrix, or a 3D or 4D tensor: it's all stored as an array. 
#
# :::{admonition} Numpy matrices
# :class: warning
# In the NumPy documentation you might also find something about *matrices*. These are no longer recommended to use: the NumPy developers advice that you use *arrays* instead, also when working in 2D.
# :::
#
# ![Numpy arrays](https://i0.wp.com/indianaiproduction.com/wp-content/uploads/2019/06/NumPy-array.png?w=1284&ssl=1)
#
# In the first chapter, you have learned about slicing and indexing of lists and tuples. Slicing in a NumPy array is very similar as in a list
#
# ## Vectors
# Vectors are easily defined by listing the entries separated by commas or spaces, e.g., ```v = [11, 12, 13]```. The number of entries of a vector is known as the *length* of the vector. Each array also has a shape, which in the case of a vector, has only one value (which is the same as the length). Each value in an array is called an *element*. You can always find out the shape of your vector by asking for its `shape` attribute.

# +
import numpy as np

v = np.array([-1, np.sin(3), 7])
print(v)
print(len(v))
print(v.shape)
# -

# A vector can be multiplied with a scalar (a number) and added to or subtracted from another vector. That vector should have the same length, or NumPy will thrown an error. All these operations are carried out element-wise.

# +
v = np.array([-1, 2, 7])
w = np.array([2, 3,  4])
z = v + w                  # an element-by-element sum
print(z)

zz = z + 2                 # add 2 to every element of vector z
print(zz)
# -

# Like in a list, one can use indices to retrieve and replace element values from the array.

print(v[1])                # print second element in the array
v[1] = 4                   # change second element in the array to a 4
print(v)

# ## Row and column vectors
# By default, NumPy doesn't differentiate between row and column vectors. To explicitly make a row vector or a column vector, we should indicate which dimension should have shape 1, and which should have a shape > 1. 

v_row = np.array([[1, 3, 4]])     # look closely, you'll see two square brackets instead of one
print(v_row)
v_col = np.array([[1], [3], [4]]) # now each element has its own row
print(v_col)

# If we now wish to perform addition and subtraction with the vectors, NumPy will show some unexpected behavior. For each row in ```v_col``` (i.e., a single scalar), it will add the full row vector of ```v_row```.

print(v_row + v_col)

# Similarly, when we multiply these two 'vectors', we get a new matrix of $3 \times 3$ elements.

# ## Loading and writing data



# ## Linear algebra
# NumPy provides the `linalg` module that contains many of the functions that you will need for linear algebra.


