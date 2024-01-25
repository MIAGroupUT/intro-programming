# # Dealing with files
#
# :::{admonition} Learning goals
# :class: note
# After finishing this chapter, you are expected to
# * open files
# * load data from files
# * save data to files
# * format strings
# :::

# ## Prerequisites
# In this chapter, you will be working with files. We have set up a small file structure that you can download from TODO. Download the ZIP-file and unzip it somewhere on your computer. Remember where you have stored it.

# ## Opening a file
#

# ## A note on loading and saving
# You'll find that many packages in Python define their own functions for loading and saving of data, and that opening and closing of files happens 'under the hood'. 

# ## Print formatting
# Here something about formatting print statements 

# ## Reading files

# ## Writing files

# ## Paths
# Each file on your computer has its own pathname that can be used for loading and saving. One thing to consider when using pathnames in your code, is that the directory structure of each computer is different. If you *hard code* your pathnames (i.e., you write explicit pathnames in your code), your code might not be easy to run on some other computer. It is good practice to let the user define some base path variable somewhere, and use the `os` package to combine that path into new paths. For example, if you have data of some project organized in a directory, data is organized per patient, then one thing you can do is to make a dictionary as follows

patient_paths = {0: 'D:\projectdata\patient0',
                 1: 'D:\projectdata\patient1',
                 2: 'D:\projectdata\patient2'}
print(patient_paths)

# Alternatively, you can use the `os.path` module instead for cleaner code

# +
import os

base_path = 'D:\projectdata'
patient_paths = {0: os.path.join(base_path, 'patient0'),
                 1: os.path.join(base_path, 'patient1'),
                 2: os.path.join(base_path, 'patient2')}
print(patient_paths)
# -

# ## Listing files
# Here discuss `glob`.
#
# :::{admonition} Exercise
# :class: tip
# Use the `glob` module to list all files in.
# :::

# ### Absolute paths
#
# ### Relative paths

patient_paths = {0: 'D:\projectdata\patient0\',
                 1: 'D:\projectdata\patient1\',
                 2: 'D:\projectdata\patient2\'}

# ## Moving files

# You can of course move files using the GUI of your operating system, but you can also move files directly from within Python. For this, the `shutil` library is useful.


