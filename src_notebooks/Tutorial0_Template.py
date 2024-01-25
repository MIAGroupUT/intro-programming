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

# # Template for educational notebooks
#
# This notebook explains how this repository builds the pure Python scripts in `src_notebooks` into the teacher and the student versions.
#
# > *Nota bene:* If you want Colab to correctly show your titles in the table of contents, please only put one title per markdow block.

# ## Generating the student version - hiding solutions
#
# This repository automatically creates the notebook using the `make` command. It generates the teacher (with answers) and the student (with blanks) versions. This command relies on the tags of the cells. Add the "teacher" (resp. "student") tag to the cells you want to keep in the teacher (resp. student) version.
#
# Au revoir elina
#
# To view and change the tags of your cells, click on View --> Cell Toolbar --> Tags.
# You should now see this notebook as follows:
#
# ![Imgur](https://i.imgur.com/FJqcESo.png)
#
# <div class="alert alert-block alert-warning"><b>Blank cells:</b> Do not forget to create blank cells with the student tag if you want to leave an empty cell.</div>

# + tags=["teacher"]
image = sample["img"]
label = sample["label"]
print(label)

# + tags=["student"]
image = "TODO"
label = "TODO"
# -

# ## Change background color with HTML 
#
# When formatting a notebook with HTML, the result may be quite different depending on the runtime execution. To avoid this, instead of using markdown cell, you can generate your formatted text in a code cell as follows:

# + tags=["hide-input"] language="html"
# <div style='background-color:rgba(80,255,80,0.4); padding:20px'>
#     <b>Exercise</b>: Choose the appropriate function in 
#         <a href="https://docs.monai.io/en/stable"><code>monai</code></a> to compute the dice.
# </div>

# + [markdown] tags=["teacher", "student"]
# The main drawback is that the HTML source code is show, which may disturb the students. You can control this if you work with colab only, and decide to hide the source code of some cells before giving the link of your colab notebook to students.
#
# You can also do the same thing directly in a markdow cell, but the background color will not be displayed in Colab:
# -

# <div style='background-color:rgba(80,255,80,0.4); padding:20px'>
#     <b>Exercise</b>: Choose the appropriate function in 
#         <a href="https://docs.monai.io/en/stable"><code>monai</code></a> to compute the dice.
# </div>
