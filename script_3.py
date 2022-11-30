# One of the simplest ways to concatenate two strings is to use the + operator .
# To understand this, consider that you want to combine the following strings –
str1 = "Welcome"
str2 = "Folks"

# Simply use the + operator in between the two strings variables to combine them –
print(str1 + " " + str2)
# ------------ Run the code------------

# There we Go! Not only did we combine the two given strings
# but also introduced a space between them.

# An alternative to “+” operator is comma (“,”).
# This quite effective when you want to implement a whitespace between two datatypes.
# Let’s see how to use it –
print(str1, str2)

# Here’s another example that demonstrates how you can use comma to combine a string and an integer –
employee_id = 10110
print("Your EID:", id)

# Let's try this with the "+" operator
employee_id = 10110
print("Your EID:" + id)
# ------------ Narrator's Note: Run the code. It raises an error-------------

# Woah! There seems to be a problem. We have a TypeError. This is because you can only concatenate
# two strings using the + operator. Similarly, when you use the + between two numbers it performs
# addition. However, you cannot concatenate a string and an integer. If you do so it leads
# to a mismatch between the two variable leading to the occurrence of a TypeError!
# This brings us to the concept of string formatting in Python.

# ============= Narrator's Note: Start explaining slide 3 of the presentation [String Formatting.pptx]=======



